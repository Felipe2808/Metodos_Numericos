import math

def biseccion():
    print("\n--- MÉTODO DE BISECCIÓN ---")
    # Entrada de la función: ejemplo x**2 - 2
    f_str = input("Ingresa la función f(x): ")
    f = lambda x: eval(f_str)
    
    a = float(input("Límite inferior (a): "))
    b = float(input("Límite superior (b): "))
    tol = float(input("Tolerancia (ej. 0.0001): "))

    if f(a) * f(b) >= 0:
        print("Error: f(a) y f(b) deben tener signos opuestos.")
        return

    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0: break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print(f"Raíz aproximada: {c}")

biseccion()
