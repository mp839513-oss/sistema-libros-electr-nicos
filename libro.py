class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def mostrar_libro(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")