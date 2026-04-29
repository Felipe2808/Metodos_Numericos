"""
CASO 2: RecursionError
Explicación: La función se llama a sí misma sin fin, llenando el 'Stack'.
Salida esperada: RecursionError: maximum recursion depth exceeded
"""

def bucle_infinito(contador):
    # No hay una condición de salida (base case), por lo que la pila se llena.
    return bucle_infinito(contador + 1)

try:
    bucle_infinito(1)
except RecursionError as e:
    print(f"Error detectado: {e}")
