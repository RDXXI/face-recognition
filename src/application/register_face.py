from src.domain.face import Face
from src.infrastructure.face_repository_fs import FaceRepositoryFS
from src.infrastructure.camera_service import CameraService
import uuid


class RegisterFaceUseCase:
def __init__(self, repo: FaceRepositoryFS, camera: CameraService):
self.repo = repo
self.camera = camera


def execute(self, name: str):
image = self.camera.capture_image(show_window=True)
if image is None:
raise RuntimeError("Captura cancelada")
embedding = self.camera.get_embedding(image)
fid = str(uuid.uuid4())
face = Face(id=fid, name=name, embedding=embedding)
self.repo.save(face)
return face