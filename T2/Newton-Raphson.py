def newton_raphson():
    print("\n--- MÉTODO DE NEWTON-RAPHSON ---")
    f_str = input("Ingresa la función f(x): ")
    df_str = input("Ingresa la derivada f'(x): ")
    f = lambda x: eval(f_str)
    df = lambda x: eval(df_str)
    
    x0 = float(input("Aproximación inicial (x0): "))
    tol = float(input("Tolerancia: "))

    x = x0
    for i in range(100):
        derivada = df(x)
        if derivada == 0:
            print("Error: Derivada es cero.")
            return
        
        x_nuevo = x - f(x) / derivada
        if abs(x_nuevo - x) < tol:
            break
        x = x_nuevo
        
    print(f"Raíz aproximada: {x}")

newton_raphson()
