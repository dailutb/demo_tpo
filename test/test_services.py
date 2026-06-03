import pytest
from unittest.mock import patch
from source.core.services import crear_producto

# ── crear_producto ─────────────

# La lista que el mock va a "devolver" cuando se llame a read_data
productos = [
    {"id_producto": 1, "categoria": "Escritura", "nombre": "Lápiz negro HB", "precio_unitario": 350},
    {"id_producto": 2, "categoria": "Escritura", "nombre": "Bolígrafo azul", "precio_unitario": 500}
    ]

# Declaramos la función que testea a crear_producto()
def test_crear_producto():
    # Arrange
    nuevo_producto = {"nombre": "Hojas A4", "categoria": "Papel", "precio_unitario": 500.0}

    # usamos with con patch, de manera que cuando crea_producto invoque a 
    # read_data / write_data use el método dummy en lugar del real
    # y asi no afectar el archivo json en disco.
    with patch("core.storage.read_data", return_value=productos.copy()) as mock_read, \
        patch("core.storage.write_data", return_value=True) as mock_write:

        # Act
        resultado = crear_producto(nuevo_producto)

        # Assert — ¿retornó True?
        assert resultado == True

        # Assert — ¿write_data fue llamado con la lista correcta?
        productos_actualizados = mock_write.call_args[0][1]  # segundo argumento de write_data
        assert len(productos_actualizados) == 3
        assert productos_actualizados[-1]["id_producto"] == 3  # ID generado automáticamente
        assert productos_actualizados[-1]["nombre"] == "Hojas A4"