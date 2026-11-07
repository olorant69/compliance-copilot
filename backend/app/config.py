"""Configuration de l'application, lue depuis le fichier .env à la racine du projet."""

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# backend/app/config.py -> racine du projet = deux niveaux au-dessus de backend/app
PROJECT_ROOT = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    """Paramètres typés ; chaque champ correspond à une variable du .env (insensible à la casse)."""

    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",  # ignore les variables du .env non déclarées ici
    )

    postgres_user: str = "compliance"
    postgres_password: str = ""
    postgres_db: str = "compliance_copilot"
    postgres_host: str = "localhost"
    postgres_port: int = 5432

    ollama_base_url: str = "http://localhost:11434"

    # Délai maximal (en secondes) de chaque vérification de /health
    health_timeout_seconds: float = 2.0


@lru_cache
def get_settings() -> Settings:
    """Renvoie la configuration, lue une seule fois puis mise en cache."""
    return Settings()
