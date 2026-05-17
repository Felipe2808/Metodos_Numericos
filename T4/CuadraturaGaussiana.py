def f(x):
    return x**2

def cuadratura_gauss_2_puntos(a, b):
    # Tabla normalizada fija para n = 2 puntos en [-1, 1]
    # Nodos (raíces de Legendre)
    t1 = -0.5773502691896257  # corresponde a -1 / raiz_cuadrada(3)
    t2 = 0.5773502691896257   # corresponde a 1 / raiz_cuadrada(3)
    
    # Pesos asociados
    w1 = 1.0
    w2 = 1.0
    
    # Cambio de variable: mapear de t en [-1, 1] hacia x en [a, b]
    x1 = ((b - a) * t1 + a + b) / 2
    x2 = ((b - a) * t2 + a + b) / 2
    
    # Evaluación de la función con sus pesos correspondientes
    suma = w1 * f(x1) + w2 * f(x2)
    
    # Escalado por el Jacobiano del cambio de intervalo
    integral = ((b - a) / 2) * suma
    return integral

# Ejecución de prueba para x^2 desde 0 hasta 2
print("Resultado Cuadratura (2 pts):", cuadratura_gauss_2_puntos(0, 2))
