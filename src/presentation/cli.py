from src.infrastructure.face_repository_fs import FaceRepositoryFS
from src.infrastructure.camera_service import CameraService
from src.application.register_face import RegisterFaceUseCase
from src.application.recognize_face import RecognizeFaceUseCase


def main():
    repo = FaceRepositoryFS()
    camera = CameraService()

    while True:
        print("\n=== Face Recognition CLI v1 ===")
        print("1) Registrar rostro desde cámara")
        print("2) Reconocer desde cámara")
        print("3) Listar rostros registrados")
        print("4) Reconocer desde archivo")
        print("0) Salir")
        opt = input("> ")

        try:
            if opt == "1":
                name = input("Nombre de la persona: ")
                use_case = RegisterFaceUseCase(repo, camera)
                face = use_case.execute(name)
                print(f"Rostro registrado: {face.name} (id={face.id})")

            elif opt == "2":
                use_case = RecognizeFaceUseCase(repo, camera)
                res = use_case.execute_from_camera()
                if res:
                    print(f"Coincidencia: {res['name']} (dist={res['distance']:.4f})")
                else:
                    print("No se encontró coincidencia")

            elif opt == "3":
                faces = repo.list_all()
                if not faces:
                    print("No hay rostros registrados")
                for f in faces:
                    print(f"- {f.id} : {f.name}")

            elif opt == "4":
                path = input("Ruta al archivo de imagen: ")
                use_case = RecognizeFaceUseCase(repo, camera)
                res = use_case.execute_from_file(path)
                if res:
                    print(f"Coincidencia: {res['name']} (dist={res['distance']:.4f})")
                else:
                    print("No se encontró coincidencia")

            elif opt == "0":
                break
            else:
                print("Opción inválida")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
