import numpy as np

def gauss_jordan(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    
    for i in range(n):
        # Normalizar fila del pivote para tener un 1 en la diagonal
        pivote = A[i, i]
        A[i, :] /= pivote
        b[i] /= pivote
        
        # Hacer ceros en toda la columna actual (arriba y abajo del pivote)
        for j in range(n):
            if i != j:
                factor = A[j, i]
                A[j, :] -= factor * A[i, :]
                b[j] -= factor * b[i]
                
    return b

# Ejemplo de uso
A_matriz = [[2.0, 1.0], [1.0, -1.0]]
b_vector = [8.0, 1.0]
print("Solución Gauss-Jordan:", gauss_jordan(A_matriz, b_vector))
