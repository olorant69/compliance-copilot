# CLAUDE.md – Briefing du projet ComplianceCopilot

## Le projet
ComplianceCopilot est un assistant IA de conformité bancaire pour l'entrée en relation client.
Projet personnel de formation et vitrine professionnelle (dépôt GitHub public).
- Module 1 (V1, en cours) : assistant réglementaire (RAG) sur la LBA, l'OBA-FINMA, la CDB, l'accord FATCA CH-US, les recommandations du GAFI et les textes sur les sanctions. Réponses avec citations obligatoires.
- Module 2 (V2) : filtrage des sanctions (listes SECO, ONU, UE, OFAC), correspondance approximative de noms, analyse des alertes par l'IA, décision finale par l'analyste.
- Module 3 (V3) : analyse de dossiers KYC fictifs par des agents IA, réutilisant le filtrage des sanctions.
- Tableaux de bord Power BI alimentés par les tables de suivi PostgreSQL.

## Comment travailler avec moi (Olivier)
- Je suis analyste technique senior et expert en conformité bancaire (sanctions, KYC, FATCA). Je maîtrise SQL, Java, C# et Linux, mais je débute en IA générative, Python moderne, React et Docker.
- Réponds-moi en français.
- Avant toute action, présente ton plan en quelques lignes et attends mon accord.
- Explique brièvement chaque notion nouvelle, avec des analogies vers ce que je connais (SQL, Java, services web).
- Avance par petites étapes que je peux comprendre et tester.
- Ne fais jamais de commit ni de push sans mon accord explicite.
- Pour le métier (réglementation, sanctions, KYC), c'est moi l'expert : pose-moi la question plutôt que de supposer.

## Architecture technique
- Frontend : React + Vite (dossier `frontend/`).
- Backend : Python 3.13 + FastAPI + Pydantic (dossier `backend/`), dépendances gérées avec uv.
- Base de données : PostgreSQL + pgvector, dans Docker (Docker Compose, moteur OrbStack sur macOS).
- IA : Ollama sur le Mac (hors Docker, port 11434). Depuis un conteneur, l'adresse est `http://host.docker.internal:11434`. Plus tard, une API LLM en ligne.
- Tout appel à un modèle passe par un module d'abstraction unique : changer de modèle = changer la configuration, pas le code.
- Configuration et secrets dans `.env` (jamais versionné) ; un fichier `.env.example` documente les variables.
- Dossier d'architecture détaillé : https://claude.ai/artifact/NCAykRn3mNcVL8HzuHvmas

## Conventions
- Noms dans le code (variables, fonctions, tables) en anglais ; commentaires, documentation et messages à l'utilisateur en français.
- Python : typage, fonctions courtes, tests avec pytest.
- Messages de commit au format Conventional Commits : `feat:`, `fix:`, `docs:`, `test:`, `chore:`.
- Petits commits, un sujet par commit.

## Règles de sécurité et de conformité
- Jamais de secret (mot de passe, clé d'API, jeton) dans le code ni dans Git.
- Uniquement des données publiques (textes réglementaires, listes officielles) ou fictives. Aucune donnée client réelle.
- Toute réponse réglementaire de l'application doit citer ses sources ; sans source trouvée, l'application le dit au lieu d'inventer.
- Pour les sanctions et le KYC, l'IA propose, l'analyste décide (humain dans la boucle).
