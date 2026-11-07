"""Point d'entrée de l'API ComplianceCopilot."""

from typing import Annotated

from fastapi import Depends, FastAPI

from app import health
from app.config import Settings, get_settings

app = FastAPI(title="ComplianceCopilot API", version="0.1.0")


@app.get("/health", response_model=health.HealthReport)
def get_health(settings: Annotated[Settings, Depends(get_settings)]) -> health.HealthReport:
    """État du serveur, de PostgreSQL et d'Ollama. Répond toujours HTTP 200."""
    return health.build_report(
        database=health.check_database(settings),
        ollama=health.check_ollama(settings),
    )
