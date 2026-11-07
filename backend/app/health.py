"""Vérifications de l'état des dépendances (PostgreSQL, Ollama) pour /health."""

from typing import Literal

import httpx
import psycopg
from pydantic import BaseModel

from app.config import Settings

Status = Literal["ok", "error"]


class ComponentHealth(BaseModel):
    """État d'un composant : ok ou error, avec un détail éventuel."""

    status: Status
    detail: str | None = None


class HealthReport(BaseModel):
    """Réponse complète de GET /health."""

    status: Literal["ok", "degraded"]
    server: Status
    database: ComponentHealth
    ollama: ComponentHealth


def check_database(settings: Settings) -> ComponentHealth:
    """Ouvre une connexion PostgreSQL et exécute SELECT 1. Ne lève jamais d'exception."""
    try:
        with psycopg.connect(
            host=settings.postgres_host,
            port=settings.postgres_port,
            dbname=settings.postgres_db,
            user=settings.postgres_user,
            password=settings.postgres_password,
            connect_timeout=max(1, int(settings.health_timeout_seconds)),
        ) as conn:
            conn.execute("SELECT 1")
        return ComponentHealth(status="ok")
    except Exception as exc:  # toute erreur = base indisponible, sans planter le serveur
        return ComponentHealth(status="error", detail=_short_error(exc))


def check_ollama(settings: Settings) -> ComponentHealth:
    """Interroge GET /api/version d'Ollama. Ne lève jamais d'exception."""
    try:
        response = httpx.get(
            f"{settings.ollama_base_url}/api/version",
            timeout=settings.health_timeout_seconds,
        )
        response.raise_for_status()
        version = response.json().get("version")
        return ComponentHealth(status="ok", detail=f"version {version}")
    except Exception as exc:
        return ComponentHealth(status="error", detail=_short_error(exc))


def build_report(database: ComponentHealth, ollama: ComponentHealth) -> HealthReport:
    """Assemble le rapport : 'degraded' dès qu'un composant est en erreur."""
    all_ok = database.status == "ok" and ollama.status == "ok"
    return HealthReport(
        status="ok" if all_ok else "degraded",
        server="ok",
        database=database,
        ollama=ollama,
    )


def _short_error(exc: Exception) -> str:
    """Message d'erreur sur une ligne (type + première ligne du message)."""
    message = str(exc).strip().splitlines()[0] if str(exc).strip() else ""
    return f"{type(exc).__name__}: {message}" if message else type(exc).__name__
