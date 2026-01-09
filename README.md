# Twitch Data Pipeline

Pipeline ELT local pour analyser les streams Twitch  
(API → DuckDB → dbt).

---

## 🎯 Objectif

Collecter des données issues de l’API Twitch (jeux, streamers, viewers)
et les transformer afin de produire des tables analytiques exploitables.

---

## 🧱 Architecture

### Data Lake (simulé par des fichiers)
- `data/raw/` : données brutes extraites depuis l’API Twitch (snapshots)

### Data Warehouse (DuckDB)
- **bronze** : données brutes chargées depuis le data lake
- **silver** : données nettoyées, typées et structurées
- **marts** : tables analytiques prêtes pour l’analyse

### dbt 
dbt/
├── models/
| ├── bronze/
│ ├── silver/
│ └── marts/


##  Stack technique
- Python
- DuckDB
- dbt
- API Twitch

### Installation

```bash
git clone https://github.com/Tomsaawyer95/twitch_data_training.git
cd twitch_data_training

python -m venv .venv
source .venv/bin/activate  # Windows : .venv\Scripts\activate

pip install -r requirements.txt

### Prérequis
- Python >= 3.10
- Git


### Configuration

Creer un fichier .env à la racine du projet contenant
    TWITCH_CLIENT_ID=xxxx
    TWITCH_CLIENT_SECRET=xxxx

Les identifiants sont à créer via le portail développeur Twitch :
https://dev.twitch.tv/docs/authentication/register-app

### Lancement de l'application 

1️⃣ Extraction (snapshot API Twitch)

```bash
python extract/src/main.py
```
⚠️ L’extraction peut être relancée plusieurs fois.
Attendre la fin complète avant de passer à l’étape suivante.


2️⃣ Ingestion (tables bronze)
```bash 
python ingest/src/ingest_twitch_stream.py
```

3️⃣ Transformations (silver & marts)
```bash 
dbt run
```

## ⚡ Quick start



```bash
git clone https://github.com/Tomsaawyer95/twitch_data_training.git
cd twitch_data_training
python -m venv .venv
source .venv/bin/activate  # Windows : .venv\Scripts\activate
pip install -r requirements.txt
python extract/src/main.py
python ingest/src/ingest_twitch_stream.py
dbt run
```

# Acces à la base de donnée
```bash
duckdb steamdata\warehouse\twitch.duckdb
```

