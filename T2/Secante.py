def secante():
    print("\n--- MÉTODO DE LA SECANTE ---")
    f_str = input("Ingresa la función f(x): ")
    f = lambda x: eval(f_str)
    
    x0 = float(input("Primera aproximación (x0): "))
    x1 = float(input("Segunda aproximación (x1): "))
    tol = float(input("Tolerancia: "))

    for i in range(100):
        if abs(f(x1) - f(x0)) < 1e-12:
            break
        
        # Pendiente estimada
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        
        if abs(x2 - x1) < tol:
            break
        x0, x1 = x1, x2
        
    print(f"Raíz aproximada: {x2}")

secante()
