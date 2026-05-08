import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        # Obtener valores de la interfaz
        x_val = float(entry_x.get())
        
        x0, y0 = float(entry_x0.get()), float(entry_y0.get())
        x1, y1 = float(entry_x1.get()), float(entry_y1.get())
        x2, y2 = float(entry_x2.get()), float(entry_y2.get())

        # 1. Interpolación Lineal (usando x0 y x1)
        res_lineal = y0 + ((y1 - y0) / (x1 - x0)) * (x_val - x0)

        # 2. Interpolación Cuadrática
        b0 = y0
        b1 = (y1 - y0) / (x1 - x0)
        num2 = (y2 - y1) / (x2 - x1)
        b2 = (num2 - b1) / (x2 - x0)
        
        res_cuad = b0 + b1*(x_val - x0) + b2*(x_val - x0)*(x_val - x1)

        label_res_lineal.config(text=f"Resultado Lineal: {res_lineal:.4f}")
        label_res_cuad.config(text=f"Resultado Cuadrática: {res_cuad:.4f}")

    except ZeroDivisionError:
        messagebox.showerror("Error", "Los valores de X deben ser distintos para evitar división por cero.")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos.")

# Configuración de la Ventana
root = tk.Tk()
root.title("Calculadora de Interpolación")
root.geometry("400x450")

# Entradas de texto
tk.Label(root, text="Punto 0 (x0, y0):").pack()
frame0 = tk.Frame(root)
frame0.pack()
entry_x0 = tk.Entry(frame0, width=10); entry_x0.pack(side=tk.LEFT)
entry_y0 = tk.Entry(frame0, width=10); entry_y0.pack(side=tk.LEFT)

tk.Label(root, text="Punto 1 (x1, y1):").pack()
frame1 = tk.Frame(root)
frame1.pack()
entry_x1 = tk.Entry(frame1, width=10); entry_x1.pack(side=tk.LEFT)
entry_y1 = tk.Entry(frame1, width=10); entry_y1.pack(side=tk.LEFT)

tk.Label(root, text="Punto 2 (x2, y2):").pack()
frame2 = tk.Frame(root)
frame2.pack()
entry_x2 = tk.Entry(frame2, width=10); entry_x2.pack(side=tk.LEFT)
entry_y2 = tk.Entry(frame2, width=10); entry_y2.pack(side=tk.LEFT)

tk.Label(root, text="Valor de X a evaluar:").pack(pady=10)
entry_x = tk.Entry(root, width=15)
entry_x.pack()

# Botón y resultados
btn_calc = tk.Button(root, text="Calcular", command=calcular, bg="#4CAF50", fg="white")
btn_calc.pack(pady=20)

label_res_lineal = tk.Label(root, text="Resultado Lineal: -", font=("Arial", 10, "bold"))
label_res_lineal.pack()

label_res_cuad = tk.Label(root, text="Resultado Cuadrática: -", font=("Arial", 10, "bold"))
label_res_cuad.pack()

root.mainloop()
