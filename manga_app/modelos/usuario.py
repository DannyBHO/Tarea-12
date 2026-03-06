class Usuario:
    """
    Representa a un usuario del sistema de mangas.
    """

    def __init__(self, nombre, id_usuario):

        self.__nombre = nombre
        self.__id_usuario = id_usuario

        # Lista obligatoria para mangas prestados
        self.__mangas_prestados = []

    # =====================
    # GETTERS
    # =====================

    def obtener_nombre(self):
        return self.__nombre

    def obtener_id(self):
        return self.__id_usuario

    def obtener_mangas(self):
        return self.__mangas_prestados

    # =====================
    # MÉTODOS
    # =====================

    def agregar_manga(self, manga):
        self.__mangas_prestados.append(manga)

    def devolver_manga(self, codigo):

        for manga in self.__mangas_prestados:

            if manga.obtener_codigo() == codigo:

                self.__mangas_prestados.remove(manga)
                return manga

        return None

    def __str__(self):
        return f"Usuario: {self.__nombre} | ID: {self.__id_usuario}"