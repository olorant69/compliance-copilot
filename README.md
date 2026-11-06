# ComplianceCopilot

Assistant IA de conformité bancaire pour l'entrée en relation client.

> 🚧 Projet en cours de construction – projet personnel de formation aux technologies de l'IA.

## Modules

| Module | Description | Statut |
|---|---|---|
| 1. Assistant réglementaire | Questions en langage naturel sur la LBA, l'OBA-FINMA, la CDB, FATCA et les recommandations du GAFI, avec réponses sourcées (RAG) | En cours |
| 2. Filtrage des sanctions | Filtrage de clients fictifs contre les listes SECO, ONU, UE et OFAC ; analyse des alertes par l'IA, décision par l'analyste | Prévu |
| 3. Analyse de dossiers KYC | Analyse de dossiers clients fictifs par des agents IA, avec score de risque | Prévu |

## Technologies

- **Interface** : React
- **Serveur** : Python, FastAPI
- **Données** : PostgreSQL, pgvector
- **IA** : Ollama (modèles locaux), puis API d'un modèle en ligne
- **Tableaux de bord** : Power BI
- **Infrastructure** : Docker

## Données

Toutes les données utilisées sont **publiques** (textes réglementaires, listes officielles de sanctions) ou **fictives** (clients de test).

## Auteur


Olivier Lorant – Analyste technique et Business Analyst, conformité bancaire
