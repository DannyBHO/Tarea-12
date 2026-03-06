class Manga:
    """
    Representa un manga dentro del sistema.
    """

    def __init__(self, titulo, autor, genero, codigo):

        # Tupla obligatoria (titulo, autor)
        self.__info = (titulo, autor)

        self.__genero = genero
        self.__codigo = codigo
        self.__disponible = True

    # =====================
    # GETTERS
    # =====================

    def obtener_titulo(self):
        return self.__info[0]

    def obtener_autor(self):
        return self.__info[1]

    def obtener_genero(self):
        return self.__genero

    def obtener_codigo(self):
        return self.__codigo

    def esta_disponible(self):
        return self.__disponible

    # =====================
    # ESTADO DEL MANGA
    # =====================

    def prestar(self):
        self.__disponible = False

    def devolver(self):
        self.__disponible = True

    def __str__(self):

        estado = "Disponible" if self.__disponible else "Prestado"

        return f"{self.__info[0]} - {self.__info[1]} | Género: {self.__genero} | Código: {self.__codigo} | {estado}"