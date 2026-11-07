# data/corpus

Textes sources de l'assistant réglementaire (RAG) : LBA, OBA-FINMA, LTPM, CDB 20, accords FATCA CH-US
(modèles 2 et 1), recommandations du GAFI, loi sur les embargos et ordonnance Ukraine.

## Règles
- Uniquement des documents publics et officiels. Aucune donnée client réelle.
- Chaque document doit permettre de citer sa source (titre, version, date, URL d'origine).

## Inventaire
Le fichier [`sources.yaml`](sources.yaml) décrit chaque document : source officielle, numéro RS, état,
dates de validité, droits et points d'attention pour les mises à jour.

## Fichiers PDF
Les PDF **ne sont pas versionnés** (voir `.gitignore`) : certains documents (GAFI, ASB) sont soumis à
des droits de diffusion. Pour reconstituer le corpus, télécharger chaque document à la source indiquée
dans `sources.yaml` et l'enregistrer ici sous le nom du champ `fichier`.

## Mises à jour prévues
- 1er janvier 2027 : entrée en vigueur de l'accord FATCA modèle 1, révision de l'OBA-FINMA et de la CDB.
- Ordonnance Ukraine : modifications fréquentes, à vérifier régulièrement.
