import tkinter as tk
from tkinter import messagebox
import numpy as np

def resolver_gauss():
    try:
        # Obtener texto y convertir a matriz numérica
        texto = entrada.get("1.0", tk.END).strip()
        lineas = texto.split('\n')
        matriz = np.array([list(map(float, l.split())) for l in lineas], dtype=float)
        
        n = len(matriz)
        
        # --- PROCESO DE ELIMINACIÓN ---
        for i in range(n):
            # Búsqueda de pivote (evitar división por cero)
            if matriz[i][i] == 0:
                messagebox.showerror("Error", "Cero en la diagonal. El método requiere pivoteo.")
                return
                
            for j in range(i + 1, n):
                factor = matriz[j][i] / matriz[i][i]
                matriz[j] = matriz[j] - factor * matriz[i]
        
        # --- SUSTITUCIÓN HACIA ATRÁS ---
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            suma = np.dot(matriz[i][i+1:n], x[i+1:n])
            x[i] = (matriz[i][-1] - suma) / matriz[i][i]
        
        # Formatear resultado
        res_texto = "\n".join([f"x{i+1} = {val:.4f}" for i, val in enumerate(x)])
        label_res.config(text=f"SOLUCIÓN:\n{res_texto}", fg="blue")
        
    except Exception as e:
        messagebox.showerror("Error", "Formato incorrecto. Use solo números y espacios.")

# Configuración Ventana
root = tk.Tk()
root.title("Eliminación Gaussiana")
root.geometry("400x450")

# Documentación en pantalla
instrucciones = (
    "COMO INGRESAR DATOS:\n"
    "1. Ingrese la matriz aumentada (coeficientes + constantes).\n"
    "2. Use espacios entre números y un 'Enter' por fila.\n"
    "Ejemplo (2x+y=5, x+2y=5):\n"
    "2 1 5\n1 2 5"
)
tk.Label(root, text=instrucciones, justify="left", fg="green", font=("Arial", 9)).pack(pady=10)

entrada = tk.Text(root, height=8, width=40)
entrada.pack(pady=5)

tk.Button(root, text="Resolver por Gauss", command=resolver_gauss, bg="lightblue").pack(pady=10)

label_res = tk.Label(root, text="Esperando datos...", font=("Arial", 10, "bold"))
label_res.pack(pady=10)

root.mainloop()
