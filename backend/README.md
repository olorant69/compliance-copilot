# backend

API de ComplianceCopilot, écrite en Python 3.13 avec FastAPI et Pydantic.
Les dépendances sont gérées avec uv (`pyproject.toml`, versions figées dans `uv.lock`).

## Démarrer

Prérequis : uv installé (`brew install uv`), fichier `.env` à la racine du projet, base PostgreSQL lancée (`docker compose up -d`) et Ollama démarré.

```bash
cd backend
uv sync                                   # crée .venv/ et installe les dépendances
uv run uvicorn app.main:app --reload      # serveur sur http://127.0.0.1:8000
uv run pytest                             # tests
```

Documentation interactive de l'API : http://127.0.0.1:8000/docs

## Points d'entrée

- `GET /health` : état du serveur, de PostgreSQL et d'Ollama. Répond toujours HTTP 200 ;
  `status` vaut `degraded` si la base ou Ollama ne répondent pas.

## Structure

- `app/main.py` : application FastAPI et routes.
- `app/config.py` : configuration lue depuis `../.env`.
- `app/health.py` : vérifications de PostgreSQL et d'Ollama.
- `tests/` : tests pytest.

À venir : assistant réglementaire, module d'abstraction des modèles d'IA, accès pgvector, filtrage des sanctions et analyse KYC.
