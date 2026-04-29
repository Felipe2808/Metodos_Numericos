import tkinter as tk
from tkinter import messagebox
import numpy as np

def resolver_jordan():
    try:
        lineas = entrada.get("1.0", tk.END).strip().split('\n')
        matriz = np.array([list(map(float, l.split())) for l in lineas], dtype=float)
        
        n = len(matriz)
        for i in range(n):
            # Hacer que el pivote sea 1
            matriz[i] = matriz[i] / matriz[i][i]
            
            # Hacer ceros arriba y abajo del pivote
            for j in range(n):
                if i != j:
                    matriz[j] = matriz[j] - matriz[j][i] * matriz[i]
        
        soluciones = matriz[:, -1]
        res_texto = "\n".join([f"x{i+1} = {val:.4f}" for i, val in enumerate(soluciones)])
        label_res.config(text=f"SOLUCIÓN:\n{res_texto}", fg="darkred")
        
    except:
        messagebox.showerror("Error", "Asegúrese de que la matriz sea cuadrada y tenga solución.")

root = tk.Tk()
root.title("Método Gauss-Jordan")
root.geometry("400x450")

tk.Label(root, text="GUÍA: Ingrese filas separadas por Enter.\nCada número separado por un espacio.", fg="purple").pack(pady=10)
entrada = tk.Text(root, height=8, width=40)
entrada.pack()

tk.Button(root, text="Calcular Gauss-Jordan", command=resolver_jordan).pack(pady=10)
label_res = tk.Label(root, text="", font=("Courier", 10))
label_res.pack()

root.mainloop()
