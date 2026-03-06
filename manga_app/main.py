from servicios.manga_servicio import MangaServicio


def menu():

    sistema = MangaServicio()

    while True:

        print("\n===== SISTEMA DE MANGAS =====")
        print("1. Agregar manga")
        print("2. Eliminar manga")
        print("3. Registrar usuario")
        print("4. Eliminar usuario")
        print("5. Prestar manga")
        print("6. Devolver manga")
        print("7. Buscar manga por título")
        print("8. Buscar manga por autor")
        print("9. Buscar manga por género")
        print("10. Ver mangas de usuario")
        print("0. Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":

            titulo = input("Título: ")
            autor = input("Autor: ")
            genero = input("Género: ")
            codigo = input("Código: ")

            sistema.agregar_manga(titulo, autor, genero, codigo)

        elif opcion == "2":

            codigo = input("Código del manga: ")
            sistema.eliminar_manga(codigo)

        elif opcion == "3":

            nombre = input("Nombre usuario: ")
            id_usuario = input("ID usuario: ")

            sistema.registrar_usuario(nombre, id_usuario)

        elif opcion == "4":

            id_usuario = input("ID usuario: ")
            sistema.eliminar_usuario(id_usuario)

        elif opcion == "5":

            id_usuario = input("ID usuario: ")
            codigo = input("Código manga: ")

            sistema.prestar_manga(id_usuario, codigo)

        elif opcion == "6":

            id_usuario = input("ID usuario: ")
            codigo = input("Código manga: ")

            sistema.devolver_manga(id_usuario, codigo)

        elif opcion == "7":

            titulo = input("Título: ")
            sistema.buscar_por_titulo(titulo)

        elif opcion == "8":

            autor = input("Autor: ")
            sistema.buscar_por_autor(autor)

        elif opcion == "9":

            genero = input("Género: ")
            sistema.buscar_por_genero(genero)

        elif opcion == "10":

            id_usuario = input("ID usuario: ")
            sistema.mangas_usuario(id_usuario)

        elif opcion == "0":

            print("Sistema finalizado")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()