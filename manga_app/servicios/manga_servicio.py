from modelos.manga import Manga
from modelos.usuario import Usuario


class MangaServicio:
    """
    Contiene toda la lógica del sistema de mangas.
    """

    def __init__(self):

        # Diccionario obligatorio
        # clave = codigo
        # valor = objeto Manga
        self.catalogo = {}

        # usuarios registrados
        self.usuarios = {}

        # set obligatorio para IDs únicos
        self.ids_usuarios = set()

    # =====================
    # MANGAS
    # =====================

    def agregar_manga(self, titulo, autor, genero, codigo):

        if codigo in self.catalogo:
            print(" El manga ya existe")
            return

        manga = Manga(titulo, autor, genero, codigo)

        self.catalogo[codigo] = manga

        print(" Manga agregado al catálogo")

    def eliminar_manga(self, codigo):

        if codigo in self.catalogo:

            del self.catalogo[codigo]
            print("Manga eliminado")

        else:
            print("Manga no encontrado")

    # =====================
    # USUARIOS
    # =====================

    def registrar_usuario(self, nombre, id_usuario):

        if id_usuario in self.ids_usuarios:
            print(" ID ya registrado")
            return

        usuario = Usuario(nombre, id_usuario)

        self.usuarios[id_usuario] = usuario
        self.ids_usuarios.add(id_usuario)

        print(" Usuario registrado")

    def eliminar_usuario(self, id_usuario):

        if id_usuario in self.usuarios:

            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)

            print("Usuario eliminado")

        else:
            print("Usuario no encontrado")

    # =====================
    # PRÉSTAMOS
    # =====================

    def prestar_manga(self, id_usuario, codigo):

        if id_usuario not in self.usuarios:
            print("Usuario no existe")
            return

        if codigo not in self.catalogo:
            print("Manga no existe")
            return

        manga = self.catalogo[codigo]

        if not manga.esta_disponible():
            print("Manga no disponible")
            return

        usuario = self.usuarios[id_usuario]

        manga.prestar()
        usuario.agregar_manga(manga)

        print("📖 Manga prestado")

    def devolver_manga(self, id_usuario, codigo):

        if id_usuario not in self.usuarios:
            print("Usuario no existe")
            return

        usuario = self.usuarios[id_usuario]

        manga = usuario.devolver_manga(codigo)

        if manga:

            manga.devolver()
            print("Manga devuelto")

        else:
            print("El usuario no tiene ese manga")

    # =====================
    # BÚSQUEDAS
    # =====================

    def buscar_por_titulo(self, titulo):

        for manga in self.catalogo.values():

            if titulo.lower() in manga.obtener_titulo().lower():

                print(manga)

    def buscar_por_autor(self, autor):

        for manga in self.catalogo.values():

            if autor.lower() in manga.obtener_autor().lower():

                print(manga)

    def buscar_por_genero(self, genero):

        for manga in self.catalogo.values():

            if genero.lower() in manga.obtener_genero().lower():

                print(manga)

    # =====================
    # LISTAR MANGAS DE USUARIO
    # =====================

    def mangas_usuario(self, id_usuario):

        if id_usuario not in self.usuarios:
            print("Usuario no existe")
            return

        usuario = self.usuarios[id_usuario]

        mangas = usuario.obtener_mangas()

        if not mangas:
            print("No tiene mangas prestados")
            return

        for manga in mangas:
            print(manga)
