def f(x):
    return x**2  # Modifica aquí tu función

def trapecio_compuesto(a, b, n):
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        x_i = a + i * h
        suma += 2 * f(x_i)
    return (h / 2) * suma

print("--- REGLA DEL TRAPECIO COMPUESTO ---")
try:
    limite_a = float(input("Ingresa el límite inferior (a): "))
    limite_b = float(input("Ingresa el límite superior (b): "))
    segmentos = int(input("Ingresa el número de subintervalos (n): "))
    
    if segmentos <= 0:
        print("[Error]: El número de segmentos debe ser mayor a 0.")
    else:
        resultado = trapecio_compuesto(limite_a, limite_b, segmentos)
        print(f"\nResultado Decimal: {resultado:.6f}")
        print(f"Cifras Significativas: {resultado:.5e}")
except ValueError:
    print("[Error]: Introduce datos numéricos válidos.")
