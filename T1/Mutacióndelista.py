"""
CASO 4: Error Lógico (Mutación de lista)
Explicación: Al borrar elementos mientras se itera, el índice interno se desfasa.
Salida esperada: [2, 3, 4] (El '2' se salta la comprobación)
"""

numeros = [1, 2, 3, 4]

# Al borrar el '1' (índice 0), el '2' pasa a ser el nuevo índice 0.
# Pero el ciclo 'for' avanza automáticamente al índice 1 (donde ahora está el 3).
for n in numeros:
    if n < 3:
        numeros.remove(n)

print(f"Resultado final inesperado: {numeros} <-- El 2 sobrevivió por el desfase de índice.")
