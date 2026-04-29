import tkinter as tk
import numpy as np

def resolver_jacobi():
    try:
        lineas = entrada.get("1.0", tk.END).strip().split('\n')
        matriz = np.array([list(map(float, l.split())) for l in lineas], dtype=float)
        
        A = matriz[:, :-1]
        b = matriz[:, -1]
        n = len(b)
        x = np.zeros(n) # Valor inicial (ceros)
        iteraciones = 100
        
        for _ in range(iteraciones):
            x_nuevo = np.zeros(n)
            for i in range(n):
                # Sumar todos los A[i][j]*x[j] excepto cuando i == j
                suma = sum(A[i][j] * x[j] for j in range(n) if i != j)
                x_nuevo[i] = (b[i] - suma) / A[i][i]
            x = x_nuevo

        res_texto = "\n".join([f"x{i+1} = {val:.6f}" for i, val in enumerate(x)])
        label_res.config(text=f"Resultado tras 100 iteraciones:\n{res_texto}")
    except:
        label_res.config(text="Error: Revisa los datos")

root = tk.Tk()
root.title("Iteración de Jacobi")
tk.Label(root, text="Instrucciones: Ingrese la matriz aumentada.\nEl sistema debe ser convergente.", justify="center").pack(pady=5)
entrada = tk.Text(root, height=10, width=40)
entrada.pack()
tk.Button(root, text="Iniciar Jacobi", command=resolver_jacobi).pack(pady=10)
label_res = tk.Label(root, text="")
label_res.pack()
root.mainloop()
