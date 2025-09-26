from typing import Optional
import numpy as np
from src.infrastructure.face_repository_fs import FaceRepositoryFS
from src.infrastructure.camera_service import CameraService


class RecognizeFaceUseCase:
def __init__(self, repo: FaceRepositoryFS, camera: CameraService, tolerance: float = 0.5):
self.repo = repo
self.camera = camera
self.tolerance = tolerance


def execute_from_camera(self):
image = self.camera.capture_image(show_window=True)
if image is None:
raise RuntimeError("Captura cancelada")
emb = np.array(self.camera.get_embedding(image))
ids, names, embeddings = self.repo.find_all_embeddings()
if not embeddings:
return None
known = np.array(embeddings)


dists = np.linalg.norm(known - emb, axis=1)
idx = int(np.argmin(dists))
if dists[idx] <= self.tolerance:
return {
"id": ids[idx],
"name": names[idx],
"distance": float(dists[idx])
}
return None


def execute_from_file(self, file_path: str):
emb = np.array(self.camera.embedding_from_file(file_path))
ids, names, embeddings = self.repo.find_all_embeddings()
if not embeddings:
return None
known = np.array(embeddings)
dists = np.linalg.norm(known - emb, axis=1)
idx = int(np.argmin(dists))
if dists[idx] <= self.tolerance:
return {
"id": ids[idx],
"name": names[idx],
"distance": float(dists[idx])
}
return None