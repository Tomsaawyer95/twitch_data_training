from pathlib import Path
import duckdb
import shutil


# Fichier courant
CURRENT_FILE = Path(__file__).resolve()

# Racine du projet (1 niveau au-dessus de ingest/)
PROJECT_ROOT = CURRENT_FILE.parents[2]


# Chemins absolus et fiables
DATA_LAKE = PROJECT_ROOT / "data" / "data_lake"
RAW_DIR = DATA_LAKE / "raw" / "twitch" / "streams"
ARCHIVE_DIR = DATA_LAKE / "archive" / "twitch" / "streams"

SQL_PATH = PROJECT_ROOT / "ingest" / "sql" / "load_bronze_twitch_streams.sql"
DB_PATH = PROJECT_ROOT / "data" / "warehouse" / "twitch.duckdb"


SQL_PATH_CREATE_TABLE = PROJECT_ROOT / "ingest" / "sql" / "create_bronze_twitch_streams.sql"


ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

conn = duckdb.connect(DB_PATH)

sql = Path(SQL_PATH_CREATE_TABLE).read_text()
conn.execute(sql)

sql = Path(SQL_PATH).read_text()

for file in RAW_DIR.glob("**/*.json"):
    try:
        print(f"Ingesting {file}")

        conn.execute(sql, [str(file), str(file)])

        target = ARCHIVE_DIR / file.relative_to(RAW_DIR)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(file, target)

        print(f"Archived {file}")

    except Exception as e:
        print(f"FAILED on {file}: {e}")
        # fichier NON déplacé → rejouable
        break

conn.close()