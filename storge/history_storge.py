import json
from pathlib import Path

class JsonStorage:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
    def save(self, data: list) -> None:
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def load(self) -> list:
        if not self.file_path.exists():
            return []

        with self.file_path.open("r", encoding="utf-8") as file:
            if file.read().strip() == "":
                return []
            file.seek(0)
            return json.load(file)
        
    def delete_history(self):
        self.save([])