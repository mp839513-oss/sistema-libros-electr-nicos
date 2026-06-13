class Usuario:

    def __init__(self, nombre, correo):
        self.__nombre = nombre
        self.__correo = correo

    def mostrar_datos(self):
        print("Nombre:", self.__nombre)
        print("Correo:", self.__correo)

        