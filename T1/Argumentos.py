"""
CASO 5: Comportamiento Inesperado de Argumentos
Explicación: Los valores por defecto se crean al DEFINIR la función, no al ejecutarla.
Salida esperada: [1] y luego [1, 2] (en lugar de solo [2])
"""

def lista_persistente(valor, mi_lista=[]):
    # 'mi_lista' apunta siempre a la misma dirección de memoria 
    # que se creó cuando el intérprete leyó la línea 'def'.
    mi_lista.append(valor)
    return mi_lista

print(f"Llamada 1: {lista_persistente(1)}")
print(f"Llamada 2: {lista_persistente(2)}") 
# ¿Por qué imprime [1, 2]? Porque la lista de la llamada 1 sigue existiendo.
