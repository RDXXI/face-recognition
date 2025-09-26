import argparse
from src.use_cases.register_face import register_face
from src.use_cases.recognize_face import recognize_face

def main():
    parser = argparse.ArgumentParser(description="Face Recognition CLI")
    subparsers = parser.add_subparsers(dest="command", help="Comando a ejecutar")

    register_parser = subparsers.add_parser("register", help="Registrar un nuevo rostro")
    register_parser.add_argument("--name", required=True, help="Nombre de la persona")

    recognize_parser = subparsers.add_parser("recognize", help="Reconocer un rostro desde la cámara")
    recognize_parser.add_argument("--image", help="Ruta a una imagen (opcional). Si no, usa la cámara.")

    args = parser.parse_args()

    if args.command == "register":
        register_face(args.name)
    elif args.command == "recognize":
        recognize_face(args.image)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
