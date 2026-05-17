def f(x):
    return x**4  # Modifica aquí tu función

def simpson_3_8(a, b, n):
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        x_i = a + i * h
        if i % 3 == 0:
            suma += 2 * f(x_i)
        else:
            suma += 3 * f(x_i)
    return (3 * h / 8) * suma

print("--- REGLA DE SIMPSON 3/8 ---")
try:
    limite_a = float(input("Ingresa el límite inferior (a): "))
    limite_b = float(input("Ingresa el límite superior (b): "))
    segmentos = int(input("Ingresa el número de subintervalos (n - Múltiplo de 3): "))
    
    if segmentos % 3 != 0 or segmentos <= 0:
        print("[Error]: Para Simpson 3/8, 'n' obligatoriamente debe ser MÚLTIPLO DE 3 mayor a 0.")
    else:
        resultado = simpson_3_8(limite_a, limite_b, segmentos)
        print(f"\nResultado Decimal: {resultado:.6f}")
        print(f"Cifras Significativas: {resultado:.5e}")
except ValueError:
    print("[Error]: Introduce datos numéricos válidos.")
