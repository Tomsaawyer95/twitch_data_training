# writers/raw_writer.py
import json
from pathlib import Path

class RawWriter:
    def write(self, dataset, snapshot, collected_at):
        date = collected_at[:10]
        hour = collected_at[11:13]

        path = Path(
            f"data/data_lake/raw/twitch/{dataset}/date={date}/hour={hour}"
        )
        path.mkdir(parents=True, exist_ok=True)

        file = path / "snapshot.json"
        with open(file, "w") as f:
            json.dump(snapshot, f)
