from libro import Libro

libros = []

while True:

    print("\n===== SISTEMA DE LIBROS =====")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:

            titulo = input("Título: ")
            autor = input("Autor: ")

            libro = Libro(titulo, autor)

            libros.append(libro)

            print("Libro agregado correctamente")

        elif opcion == 2:

            if len(libros) == 0:
                print("No existen libros")

            else:
                for libro in libros:
                    libro.mostrar_libro()

        elif opcion == 3:
            print("Saliendo...")
            break

        else:
            print("Opción inválida")

    except ValueError:
        print("Debe ingresar un número")
        