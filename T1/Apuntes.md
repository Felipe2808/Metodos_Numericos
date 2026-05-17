# Apuntes de Ingeniería: Análisis de Excepciones y Errores Críticos en Python

Este documento contiene la definición, la lógica algorítmica, ejemplos prácticos de código y el desarrollo analítico a mano (con resultados a 5 cifras significativas) de los errores de ejecución analizados.

---

## 1. `Argumentos.py` (Errores de Argumentos / TypeError o ValueError)

* **Definición:** Excepción que ocurre cuando los datos pasados a una función no coinciden con la cantidad, tipo o restricciones de los parámetros esperados por su diseño lógico.
* **Algoritmo (Lógica):** 1. El intérprete evalúa la firma de la función invocada.
  2. Compara el número de argumentos enviados con los requeridos.
  3. Evalúa si el tipo de objeto o su valor interno cumple con las operaciones aritméticas o lógicas internas de la función.
  4. Si alguna validación falla, detiene la ejecución y despacha la excepción antes de ejecutar el bloque interno.

### Código en Python
```python
import math

# Ejemplo 1: Incompatibilidad de tipo en función nativa
try:
    resultado_1 = len(12345.6)
except TypeError as e:
    print(f"Error 1: {e}")

# Ejemplo 2: Valor fuera de dominio matemático legítimo
try:
    resultado_2 = math.sqrt(-25.0)
except ValueError as e:
    print(f"Error 2: {e}")

# Ejemplo 3: División con tipos incompatibles
try:
    resultado_3 = 50.0 / "2.5"
except TypeError as e:
    print(f"Error 3: {e}")
