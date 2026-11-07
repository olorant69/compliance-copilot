"""Tests de GET /health, sans dépendre de Docker ni d'Ollama."""

import pytest
from fastapi.testclient import TestClient

from app import health
from app.config import Settings, get_settings
from app.health import ComponentHealth
from app.main import app

OK = ComponentHealth(status="ok")
DOWN = ComponentHealth(status="error", detail="simulé")


@pytest.fixture
def client():
    yield TestClient(app)
    app.dependency_overrides.clear()


def _simulate(monkeypatch, database: ComponentHealth, ollama: ComponentHealth) -> None:
    """Remplace les vraies vérifications par des résultats simulés (comme un mock Mockito)."""
    monkeypatch.setattr(health, "check_database", lambda settings: database)
    monkeypatch.setattr(health, "check_ollama", lambda settings: ollama)


def test_health_all_ok(client, monkeypatch):
    _simulate(monkeypatch, database=OK, ollama=OK)

    response = client.get("/health")

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["server"] == "ok"
    assert body["database"]["status"] == "ok"
    assert body["ollama"]["status"] == "ok"


@pytest.mark.parametrize(
    ("database", "ollama"),
    [(DOWN, OK), (OK, DOWN), (DOWN, DOWN)],
    ids=["base-en-panne", "ollama-en-panne", "tout-en-panne"],
)
def test_health_degraded_still_200(client, monkeypatch, database, ollama):
    _simulate(monkeypatch, database=database, ollama=ollama)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "degraded"
    assert response.json()["server"] == "ok"


def test_health_unreachable_services_do_not_crash(client):
    """Vraies vérifications vers des adresses injoignables : le serveur doit répondre quand même."""
    unreachable = Settings(
        postgres_host="127.0.0.1",
        postgres_port=1,
        ollama_base_url="http://127.0.0.1:1",
        health_timeout_seconds=1,
    )
    app.dependency_overrides[get_settings] = lambda: unreachable

    response = client.get("/health")

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "degraded"
    assert body["database"]["status"] == "error"
    assert body["ollama"]["status"] == "error"
    assert body["database"]["detail"]
