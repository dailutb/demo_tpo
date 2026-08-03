import re
from shared import utilities
from core import storage
from config import *


# Funcion generar id_producto
def generar_id_producto(productos):
    if not productos:  # lista vacía
        return 1
    max_id = max(productos, key=lambda p: p["id_producto"])
    return max_id["id_producto"] + 1


# Funcion persistir producto
def crear_producto(producto):
    # Recuperamos los datos del archivo
    productos = storage.read_data(RUTA_PRODUCTOS)
    # Generamos el id_producto (PK), insertamos en memoria
    producto["id_producto"] = generar_id_producto(productos)
    productos.append(producto)
    # Persistimos en disco
    storage.write_data(RUTA_PRODUCTOS, productos)
    return True


# Funcion get_productos
# Parametros: None
# Retorno: productos:list
def get_productos():
    # Recuperamos los datos del archivo
    print(RUTA_PRODUCTOS)
    productos = storage.read_data(RUTA_PRODUCTOS)
    # Búsqueda con lista por comprensión
    return productos

# Funcion get_producto_by_id
# Parametros: id_producto:int
# Retorno: productos:list
def get_producto_by_id(id_producto):
    # Recuperamos los datos del archivo
    productos = storage.read_data(RUTA_PRODUCTOS)
    # Búsqueda con lista por comprensión
    productos_found = [producto for producto in productos if re.fullmatch(str(id_producto), str(producto["id_producto"]))]
    return productos_found

# Funcion get_producto_by_nombre
# Parametros: nombre:str
# Retorno: productos_encontrados:list
def get_producto_by_nombre(nombre):
    # Recuperamos los datos del archivo
    productos = storage.read_data(RUTA_PRODUCTOS)
    # Búsqueda con lista por comprensión
    productos_found = [producto for producto in productos if re.search(nombre, producto["nombre"], re.IGNORECASE)]
    # Retornamos la lista, vacía o con los registros encontrados
    return productos_found

# Funcion update_producto_by_id
# Parametros: id_producto:int, producto:dict
# Retorno: True si se actualizó, False si no se encontró el id_producto
def update_producto_by_id(id_producto, producto):
    # Recuperamos los datos del archivo
    productos = storage.read_data(RUTA_PRODUCTOS)
    # Buscamos el índice del producto a actualizar
    for i, p in enumerate(productos):
        if p["id_producto"] == id_producto:
            producto["id_producto"] = id_producto
            productos[i] = producto
            storage.write_data(RUTA_PRODUCTOS, productos)
            return True
    return False

# Funcion delete_producto
# Parametros: id_producto:int
# Retorno: True si se eliminó, False si no se encontró el id_producto
def delete_producto(id_producto):
    # Recuperamos los datos del archivo
    productos = storage.read_data(RUTA_PRODUCTOS)
    # Filtramos excluyendo el producto a eliminar
    productos_restantes = [p for p in productos if p["id_producto"] != id_producto]
    if len(productos_restantes) == len(productos):
        return False
    storage.write_data(RUTA_PRODUCTOS, productos_restantes)
    return True

