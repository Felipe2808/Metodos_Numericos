"""
CASO 3: OverflowError (Floats)
Explicación: Los números decimales (float) tienen un límite físico de 64 bits.
Salida esperada: OverflowError: (34, 'Numerical result out of range')
"""

try:
    # Los enteros en Python son infinitos, pero al usar '2.0' (float),
    # el resultado debe seguir la norma IEEE 754.
    exponente_limite = 2.0**2000 
    print(exponente_limite)
except OverflowError as e:
    print(f"Error: El número decimal es demasiado grande para Python: {e}")
