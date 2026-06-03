# Demo proyecto
# La idea es que vayan analizando la estructura de archivos para su proyecto
# Para ejecutarlo pararse en Demo_TPO/source y ejecutar en consola python -m app.main

# Importamos librerias externas
from tabulate import tabulate
from core import services
from core import storage
from interface import inputHandler
from config import *

# Declaración de la Funcion Principal
def main():
    print("Bienvenido!!")

    while True:
        print("""
    Ingrese:
    1. Para crear un nuevo producto
    2. Para listar todos los productos
    3. Para buscar producto por id_producto
    4. Para buscar producto por nombre de producto
    5. Para salir
            """)
        opcion = input("Ingrese su opción: ")
        match opcion:
            case "1":
                # Alta de producto
                try:
                    producto = inputHandler.leer_producto()
                    response = services.crear_producto(producto)
                    print("Producto insertado exitosamente") if response else None
                except Exception as e:
                    print(f"Error al crear el producto: {e}")

            case "2":
                # Listar productos
                try:
                    productos = services.get_productos()
                    print(tabulate(productos[:5], headers="keys", tablefmt="grid"))
                except Exception as e:
                    print(f"Error al listar productos: {e}")

            case "3":
                # Buscar producto por id_producto
                try:
                    id_producto = int(input("Ingrese el id_producto a buscar: "))
                except ValueError:
                    print("ID inválido, debe ser un número entero.")
                    continue
                productos_found = services.get_producto_by_id(id_producto)
                if productos_found:
                    print(tabulate(productos_found, headers="keys", tablefmt="grid"))
                else:
                    print("No match")

            case "4":
                # buscar producto por nombre de producto
                try:
                    nombre = input("Ingrese el nombre del producto a buscar - total o parcial: ")
                    productos_found = services.get_producto_by_nombre(nombre)
                    print(tabulate(productos_found[:5], headers="keys", tablefmt="grid"))
                except Exception as e:
                    print(f"Error al buscar producto por nombre: {e}")

                
            case "5":
                # Terminar App
                print("Saliendo...")
                break
            case _:
                print("Opción inválida, intente nuevamente...")


# Invocar a la función principal
if __name__ == "__main__":

    try:
        storage.inicializar_storage(RUTA_PRODUCTOS)
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
