import math

# Ejercicio 1: f(x) = x^4 - 3x^2
def f_diff1(x):
    return x**4 - 3*x**2

# Ejercicio 2: f(x) = ln(x)
def f_diff2(x):
    return math.log(x)

# Ejercicio 3: f(x) = exp(-x^2)
def f_diff3(x):
    return math.exp(-x**2)

def diff_cinco_puntos(f, x, h):
    numerador = -f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)
    return numerador / (12 * h)

# Ejecuciones
print(f"Derivada Ej1: {diff_cinco_puntos(f_diff1, 1.0, 0.1):.5g}")
print(f"Derivada Ej2: {diff_cinco_puntos(f_diff2, 2.0, 0.01):.5g}")
print(f"Derivada Ej3: {diff_cinco_puntos(f_diff3, 0.5, 0.1):.5g}")
