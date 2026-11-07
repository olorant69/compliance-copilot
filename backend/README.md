# backend

API de ComplianceCopilot, écrite en Python 3.13 avec FastAPI et Pydantic.
Les dépendances sont gérées avec uv.

Ce dossier contiendra :
- les points d'entrée de l'API (assistant réglementaire, puis filtrage des sanctions et analyse KYC) ;
- le module d'abstraction unique pour les appels aux modèles d'IA (Ollama, puis une API en ligne) ;
- l'accès à PostgreSQL + pgvector ;
- les tests pytest.
