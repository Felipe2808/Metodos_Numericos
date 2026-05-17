import numpy as np

def gauss_seidel(A, b, x0, tol=1e-5, max_iter=100):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x = np.array(x0, dtype=float)
    n = len(b)
    
    for k in range(max_iter):
        x_viejo = x.copy()
        
        for i in range(n):
            # Suma de los elementos ya actualizados y los antiguos
            suma = 0.0
            for j in range(n):
                if i != j:
                    suma += A[i, j] * x[j]
            
            # El nuevo valor calculado sustituye de inmediato en el vector x
            x[i] = (b[i] - suma) / A[i, i]
            
        # Criterio de parada basado en norma infinita
        if np.max(abs(x - x_viejo)) < tol:
            return x
    return x

# Ejemplo numérico
A_matriz = [[3.0, 1.0], [1.0, 4.0]]
b_vector = [7.0, 6.0]
x_inicio = [0.0, 0.0]
print("Solución Gauss-Seidel:", gauss_seidel(A_matriz, b_vector, x_inicio))
