
import re

# Funcion validar categoria
# Parametros: categoria:string
# Retorno: True if OK o False:bool
def validar_categoria(categoria):
    patron_categoria = r"[A-Za-záéíóúÁÉÍÓÚüÜñÑ\s]+"
    return bool(re.fullmatch(patron_categoria, categoria.strip()))


# Funcion validar nombre
# Parametros: nombre:string
# Retorno: True if OK o False:bool
def validar_nombre(nombre):
    patron_nombre = r"[A-Za-z0-9áéíóúÁÉÍÓÚüÜñÑ ]+"
    return bool(re.fullmatch(patron_nombre, nombre.strip()))


# Funcion validar precio_unitario
# Parametros: precio_unitario:str
# Retorno: True if OK o False:bool
def validar_precio_unitario(precio_unitario):
    patron = r"[0-9]+(\.[0-9]{1,2})?"
    return bool(re.fullmatch(patron, precio_unitario.strip()))
