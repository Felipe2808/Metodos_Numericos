"""
CASO 1: MemoryError
Explicación: Intento de crear una estructura de datos que excede la RAM física.
Salida esperada: MemoryError
"""

try:
    # Creamos una lista multiplicando un solo elemento por un número astronómico.
    # Python intentará reservar espacio para todos estos punteros de golpe.
    bloque_masivo = [1] * (10**12) 
except MemoryError:
    print("Error: Se agotó la memoria RAM disponible para esta lista.")
