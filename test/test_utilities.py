import pytest
from source.shared.utilities import *

# ── validar_precio_unitario ─────────────

def test_validar_precio_entero_valido():
    # Arrange
    precio = "350"
    # Act
    resultado = validar_precio_unitario(precio)
    # Assert
    assert resultado == True



# ── Con parametrize: limpio y escalable ───────────────────────────
# @pytest.mark.parametrize("precio, esperado", [
#     # Happy path
#     ("350",     True),
#     ("99.99",   True),
#     ("1200.5",  True),
#     ("0",       True),
#     # Sad path
#     ("abc",     False),
#     ("-50",     False),
#     ("99.999",  False),
#     ("",        False),
#     (".99",     False),
# ])

# def test_validar_precio_parametrizado(precio, esperado):
#     assert validar_precio_unitario(precio) == esperado

