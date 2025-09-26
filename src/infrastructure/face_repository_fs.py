import json
from pathlib import Path
from typing import List, Optional
from src.domain.face import Face


class FaceRepositoryFS:
def __init__(self, path: str = "data/faces.json"):
self.path = Path(path)
if not self.path.parent.exists():
self.path.parent.mkdir(parents=True, exist_ok=True)
if not self.path.exists():
self._write({})


def _read(self) -> dict:
with open(self.path, "r", encoding="utf-8") as f:
return json.load(f)


def _write(self, data: dict):
with open(self.path, "w", encoding="utf-8") as f:
json.dump(data, f, indent=2)


def save(self, face: Face):
data = self._read()
data[face.id] = {
"name": face.name,
"embedding": face.embedding
}
self._write(data)


def list_all(self) -> List[Face]:
data = self._read()
faces = []
for fid, v in data.items():
faces.append(Face(id=fid, name=v["name"], embedding=v["embedding"]))
return faces


def find_all_embeddings(self):
data = self._read()
ids = []
names = []
embeddings = []
for fid, v in data.items():
ids.append(fid)
names.append(v["name"])
embeddings.append(v["embedding"])
return ids, names, embeddings


def get_by_id(self, id: str) -> Optional[Face]:
data = self._read()
if id in data:
v = data[id]
return Face(id=id, name=v["name"], embedding=v["embedding"])
return None