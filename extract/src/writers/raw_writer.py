# writers/raw_writer.py
import json
from pathlib import Path

# Fichier courant
CURRENT_FILE = Path(__file__).resolve()

# Racine du projet (1 niveau au-dessus de extract/)
PROJECT_ROOT = CURRENT_FILE.parents[3]
print(PROJECT_ROOT)

class RawWriter:
    def write(self, dataset, snapshot, collected_at):
        date = collected_at[:10]
        hour = collected_at[11:13]
        path = (
            PROJECT_ROOT
            / "data"
            / "data_lake"
            / "raw"
            / "twitch"
            / dataset
            / f"date={date}"
            / f"hour={hour}"
        )
        
        path.mkdir(parents=True, exist_ok=True)
        print(path)
        file = path / "snapshot.json"
        with open(file, "w") as f:
            json.dump(snapshot, f)

