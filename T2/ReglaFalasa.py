def regla_falsa():
    print("\n--- MÉTODO DE REGLA FALSA ---")
    f_str = input("Ingresa la función f(x): ")
    f = lambda x: eval(f_str)
    
    a = float(input("Límite inferior (a): "))
    b = float(input("Límite superior (b): "))
    tol = float(input("Tolerancia: "))

    for i in range(100):
        # Punto calculado por interpolación lineal
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        
        if abs(f(c)) < tol:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print(f"Raíz aproximada: {c}")

regla_falsa()
