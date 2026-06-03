from shared import utilities


# Funcion leer consola
# Parametros: none
# Retorno: diccionario producto
def leer_producto():
    # Defino máxima cantidad de intentos
    MAX_INTENTOS = 3

    # Ingresar categoria
    for intento in range(MAX_INTENTOS):
        categoria = input("Ingrese la categoria: ")
        if utilities.validar_categoria(categoria):
            break
        print("Categoría no válida, intente nuevamente...")
    else:
        raise ValueError("Se superó el máximo de intentos para categoría.")

    # Ingresar nombre
    for intento in range(MAX_INTENTOS):
        nombre = input("Ingrese el nombre: ")
        if utilities.validar_nombre(nombre):
            break
        print("Nombre no válido intente nuevamente...")
    else:
        raise ValueError("Se superó el máximo de intentos para nombre.")

    # Ingresar precio_unitario
    for intento in range(MAX_INTENTOS):
        precio_unitario = input("Ingrese el precio unitario: ")
        if utilities.validar_precio_unitario(precio_unitario):
            break
        print("Precio no válido intente nuevamente...")
    else:
        raise ValueError("Se superó el máximo de intentos para precio unitario.")

    # Normalizacion y carga en variable temporal
    producto = {
        "categoria": categoria.strip().title(),
        "nombre": nombre.strip().title(),
        "precio_unitario": float(precio_unitario.strip()),
    }

    return producto
