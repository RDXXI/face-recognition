import cv2
import numpy as np
import face_recognition


class CameraService:
def __init__(self, camera_index: int = 0):
self.camera_index = camera_index


def capture_image(self, show_window: bool = False):
cap = cv2.VideoCapture(self.camera_index)
if not cap.isOpened():
raise RuntimeError("No se pudo abrir la cámara. Revisa el índice o permisos.")


ret = False
frame = None
print("Presiona SPACE para capturar, ESC para cancelar...")


while True:
ret, frame = cap.read()
if not ret:
break
cv2.imshow("Captura - presiona SPACE", frame)
key = cv2.waitKey(1) & 0xFF
if key == 27: # ESC
frame = None
break
elif key == 32: # SPACE
break


cap.release()
cv2.destroyAllWindows()


if frame is None:
return None


rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
return rgb


def get_embedding(self, image_rgb) -> list:
boxes = face_recognition.face_locations(image_rgb)
if len(boxes) == 0:
raise ValueError("No se detectó ninguna cara en la imagen")
encodings = face_recognition.face_encodings(image_rgb, boxes)
if len(encodings) == 0:
raise ValueError("No se pudo obtener embedding de la cara")
emb = encodings[0]
return emb.tolist()


def embedding_from_file(self, file_path: str) -> list:
image = face_recognition.load_image_file(file_path)
boxes = face_recognition.face_locations(image)
if len(boxes) == 0:
raise ValueError("No se detectó ninguna cara en la imagen")
encodings = face_recognition.face_encodings(image, boxes)
return encodings[0].tolist()