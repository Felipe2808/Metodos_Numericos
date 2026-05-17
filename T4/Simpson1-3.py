def f(x):
    return x**4  # Modifica aquí tu función

def simpson_1_3(a, b, n):
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        x_i = a + i * h
        if i % 2 != 0:
            suma += 4 * f(x_i)
        else:
            suma += 2 * f(x_i)
    return (h / 3) * suma

print("--- REGLA DE SIMPSON 1/3 ---")
try:
    limite_a = float(input("Ingresa el límite inferior (a): "))
    limite_b = float(input("Ingresa el límite superior (b): "))
    segmentos = int(input("Ingresa el número de subintervalos (n - Debe ser PAR): "))
    
    if segmentos % 2 != 0 or segmentos <= 0:
        print("[Error]: Para Simpson 1/3, 'n' obligatoriamente debe ser un número PAR mayor a 0.")
    else:
        resultado = simpson_1_3(limite_a, limite_b, segmentos)
        print(f"\nResultado Decimal: {resultado:.6f}")
        print(f"Cifras Significativas: {resultado:.5e}")
except ValueError:
    print("[Error]: Introduce datos numéricos válidos.")
