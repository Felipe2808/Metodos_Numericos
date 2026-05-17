
# SISTEMAS DE ECUACIONES LINEALES 

## 1. `EliminacionGaussiana.py` (Eliminación Gaussiana con Sustitución Hacia Atrás)

* **Definición:** Método directo para resolver sistemas de ecuaciones lineales. Consiste en operar la matriz aumentada del sistema mediante transformaciones elementales por filas para transformarla en una matriz triangular superior. Una vez logrado esto, los valores de las incógnitas se calculan secuencialmente desde la última variable hasta la primera (sustitución hacia atrás).
* **Algoritmo (Lógica):**
1. Construir la matriz aumentada [A | b] combinando los coeficientes de las variables y el vector de términos independientes.
2. **Eliminación hacia adelante:** Recorrer cada columna (pivote) y, mediante operaciones de renglón (Fila_i = Fila_i - factor * Fila_pivote), hacer cero todos los elementos que estén por debajo del pivote principal.
3. Si algún elemento pivote es cero o muy cercano a cero, se debe realizar un intercambio de filas (pivoteo) para evitar la división entre cero.
4. **Sustitución hacia atrás:** Despejar la última variable del sistema y usar su valor para resolver escalonadamente hacia arriba el resto de las incógnitas.



### Código en Python

```python
import numpy as np

def eliminacion_gaussiana(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    
    # 1. Eliminación hacia adelante
    for i in range(n):
        # Pivoteo simple si el pivote es cero
        if A[i, i] == 0:
            for k in range(i + 1, n):
                if A[k, i] != 0:
                    A[[i, k]] = A[[k, i]]
                    b[[i, k]] = b[[k, i]]
                    break
        
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]
            
    # 2. Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        suma = np.dot(A[i, i+1:], x[i+1:])
        x[i] = (b[i] - suma) / A[i, i]
        
    return x

# Ejemplo de uso: Sistema de 2x2
A_matriz = [[2.0, 1.0], [1.0, -1.0]]
b_vector = [8.0, 1.0]
print("Solución:", eliminacion_gaussiana(A_matriz, b_vector))

```

### Explicación y Procedimiento a Mano

* **Ejemplo 1: Sistema 2x2: (2x + y = 8), (x - y = 1)**
* **Explicación:** Planteamos la matriz aumentada inicial y buscamos eliminar la variable `x` de la segunda fila utilizando el pivote de la primera fila.
* **A mano:** * Matriz aumentada original:
[ 2.0  1.0 | 8.0 ]
[ 1.0 -1.0 | 1.0 ]
* Paso 1 (Eliminación): El pivote es Fila 1, Columna 1 = 2.0. El factor para la Fila 2 es: 1.0 / 2.0 = 0.5.
* Nueva Fila 2 = Fila 2 - (0.5 * Fila 1) -> [1.0 - 0.5(2), -1.0 - 0.5(1) | 1.0 - 0.5(8)] = [0.0, -1.5 | -3.0].
* Matriz triangular superior resultante:
[ 2.0  1.0 |  8.0 ]
[ 0.0 -1.5 | -3.0 ]
* Paso 2 (Sustitución): Desde la última fila: -1.5 * y = -3.0 -> y = -3.0 / -1.5 = 2.0.
* Sustituyendo hacia arriba: 2x + 1(2.0) = 8.0 -> 2x = 6.0 -> x = 3.0.
* Resultado: x = 3.0000, y = 2.0000




* **Ejemplo 2: Sistema con pivoteo: (0x + 2y = 4), (3x + y = 5)**
* **Explicación:** El primer elemento de la primera fila es cero. No se puede usar como divisor, por lo que el algoritmo detecta la condición e intercambia las filas.
* **A mano:** * Matriz aumentada:
[ 0.0  2.0 | 4.0 ]
[ 3.0  1.0 | 5.0 ]
* Operación: Intercambio Fila 1 <-> Fila 2 debido a pivote nulo.
* Matriz reestructurada:
[ 3.0  1.0 | 5.0 ]
[ 0.0  2.0 | 4.0 ]
* Como el elemento debajo de la columna 1 ya es cero, la matriz ya es triangular.
* Sustitución: 2y = 4.0 -> y = 2.0. Luego: 3x + 1(2.0) = 5.0 -> 3x = 3.0 -> x = 1.0.




* **Ejemplo 3: Sistema 2x2: (4x + 3y = 10), (2x + 5y = 12)**
* **Explicación:** Eliminamos el valor por debajo del elemento matriz[0][0] = 4.0.
* **A mano:** * Matriz aumentada:
[ 4.0  3.0 | 10.0 ]
[ 2.0  5.0 | 12.0 ]
* Operación Fila 2: Factor = 2.0 / 4.0 = 0.5.
* Nueva Fila 2 = [2 - 0.5(4), 5 - 0.5(3) | 12 - 0.5(10)] = [0.0, 3.5 | 7.0].
* Sustitución: 3.5 * y = 7.0 -> y = 2.0. Luego: 4x + 3(2.0) = 10.0 -> 4x = 4.0 -> x = 1.0.





---

## 2. `GaussJordan.py` (Método de Gauss-Jordan)

* **Definición:** Extensión del método de eliminación gaussiana. En lugar de detenerse cuando la matriz es triangular superior y aplicar sustitución hacia atrás, continúa eliminando elementos tanto por debajo como por **encima** de la diagonal principal, al mismo tiempo que normaliza los pivotes a 1. El objetivo es transformar la matriz original directamente en la matriz identidad, dejando las soluciones calculadas directamente en el vector de términos independientes.
* **Algoritmo (Lógica):**
1. Preparar la matriz aumentada [A | b].
2. Seleccionar el pivote de la columna actual de la diagonal principal.
3. Dividir toda la fila del pivote entre el valor del propio pivote, haciendo que dicho elemento valga exactamente 1 (normalización).
4. Para todas las demás filas (tanto superiores como inferiores), restar un múltiplo de la fila pivote para transformar el resto de los elementos de esa columna en ceros perfectos.
5. Repetir el proceso para cada columna hasta completar la diagonal. Al finalizar, la parte izquierda será la matriz identidad, y la parte derecha contendrá las variables resueltas.



### Código en Python

```python
import numpy as np

def gauss_jordan(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    
    for i in range(n):
        # Normalizar fila del pivote para tener un 1 en la diagonal
        pivote = A[i, i]
        A[i, :] /= pivote
        b[i] /= pivote
        
        # Hacer ceros en toda la columna actual (arriba y abajo del pivote)
        for j in range(n):
            if i != j:
                factor = A[j, i]
                A[j, :] -= factor * A[i, :]
                b[j] -= factor * b[i]
                
    return b

# Ejemplo de uso
A_matriz = [[2.0, 1.0], [1.0, -1.0]]
b_vector = [8.0, 1.0]
print("Solución Gauss-Jordan:", gauss_jordan(A_matriz, b_vector))

```

### Explicación y Procedimiento a Mano

* **Ejemplo 1: Sistema 2x2: (2x + y = 8), (x - y = 1)**
* **Explicación:** Llevaremos la matriz de coeficientes a la forma identidad paso a paso, normalizando renglones.
* **A mano:** * Matriz aumentada inicial:
[ 2.0  1.0 | 8.0 ]
[ 1.0 -1.0 | 1.0 ]
* Operación 1: Normalizar Fila 1 dividiendo entre su pivote (2.0) -> Nueva Fila 1 = [1.0, 0.5 | 4.0].
* Operación 2: Hacer cero la posición debajo del pivote en Fila 2. Fila 2 = Fila 2 - 1.0 * Fila 1.
Fila 2 nueva = [1.0 - 1(1.0), -1.0 - 1(0.5) | 1.0 - 1(4.0)] = [0.0, -1.5 | -3.0].
* Matriz intermedia:
[ 1.0  0.5 |  4.0 ]
[ 0.0 -1.5 | -3.0 ]
* Operación 3: Normalizar Fila 2 dividiendo entre su propio pivote (-1.5) -> Nueva Fila 2 = [0.0, 1.0 | 2.0].
* Operación 4: Hacer cero la posición arriba del pivote en Fila 1. Fila 1 = Fila 1 - 0.5 * Fila 2.
Fila 1 nueva = [1.0 - 0.5(0), 0.5 - 0.5(1) | 4.0 - 0.5(2.0)] = [1.0, 0.0 | 3.0].
* Matriz reducida final:
[ 1.0  0.0 | 3.0 ]
[ 0.0  1.0 | 2.0 ]
* Solución leída directamente: x = 3.0000, y = 2.0000




* **Ejemplo 2: Sistema 2x2: (5x - 2y = 11), (1x + 4y = 11)**
* **Explicación:** Transformamos de forma directa a matriz identidad por operaciones simétricas.
* **A mano:** * Matriz inicial:
[ 5.0 -2.0 | 11.0 ]
[ 1.0  4.0 | 11.0 ]
* Normalizar Fila 1 (/5) -> [1.0, -0.4 | 2.2].
* Limpiar columna 1 en Fila 2 (Fila 2 - 1 * Fila 1) -> [0.0, 4.4 | 8.8].
* Normalizar Fila 2 (/4.4) -> [0.0, 1.0 | 2.0].
* Limpiar columna 2 en Fila 1 (Fila 1 - (-0.4) * Fila 2) -> [1.0, 0.0 | 2.2 + 0.8] = [1.0, 0.0 | 3.0].
* Resultado directo: x = 3.0000, y = 2.0000




* **Ejemplo 3: Sistema diagonal: (2x + 0y = 6), (0x + 4y = 8)**
* **Explicación:** Si la matriz ya tiene ceros fuera de la diagonal, sólo se requiere el paso de normalización de filas.
* **A mano:** * Matriz aumentada:
[ 2.0  0.0 | 6.0 ]
[ 0.0  4.0 | 8.0 ]
* Fila 1 dividida entre 2 -> [1.0, 0.0 | 3.0]
* Fila 2 dividida entre 4 -> [0.0, 1.0 | 2.0]
* Solución implícita instantánea: x = 3.0000, y = 2.0000





---

## 3. `GaussSeidel.py` (Método de Gauss-Seidel)

* **Definición:** Método iterativo empleado para resolver sistemas de ecuaciones lineales de gran tamaño. A diferencia de los métodos directos, comienza con una aproximación inicial y refina los valores de manera iterativa. Su característica principal es que **utiliza inmediatamente los nuevos valores calculados de las variables dentro de la misma iteración en curso**, lo que acelera significativamente la convergencia. Requiere idealmente que la matriz sea diagonalmente dominante.
* **Algoritmo (Lógica):**
1. Verificar o reordenar el sistema de ecuaciones para garantizar la dominancia diagonal (|A[i,i]| > suma de los valores absolutos del resto de la fila).
2. Despejar algebraicamente cada incógnita "i" en función de las demás variables, basándose en la ecuación "i".
3. Establecer un vector de aproximaciones iniciales (usualmente ceros).
4. En la iteración actual, calcular el nuevo valor de la variable x[i].
5. **Actualización inmediata:** Al pasar al cálculo de x[i+1], usar el valor de x[i] que se acaba de actualizar en lugar del valor de la iteración anterior.
6. Evaluar el error de aproximación. Repetir hasta que el error sea menor que la tolerancia o se alcance el límite de iteraciones.



### Código en Python

```python
import numpy as np

def gauss_seidel(A, b, x0, tol=1e-5, max_iter=100):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x = np.array(x0, dtype=float)
    n = len(b)
    
    for k in range(max_iter):
        x_viejo = x.copy()
        
        for i in range(n):
            # Suma de los elementos ya actualizados y los antiguos
            suma = 0.0
            for j in range(n):
                if i != j:
                    suma += A[i, j] * x[j]
            
            # El nuevo valor calculado sustituye de inmediato en el vector x
            x[i] = (b[i] - suma) / A[i, i]
            
        # Criterio de parada basado en norma infinita
        if np.max(abs(x - x_viejo)) < tol:
            return x
    return x

# Ejemplo numérico
A_matriz = [[3.0, 1.0], [1.0, 4.0]]
b_vector = [7.0, 6.0]
x_inicio = [0.0, 0.0]
print("Solución Gauss-Seidel:", gauss_seidel(A_matriz, b_vector, x_inicio))

```

### Explicación y Procedimiento a Mano

* **Ejemplo 1: Sistema: (3x + y = 7), (x + 4y = 6) con semilla inicial [0.0, 0.0]**
* **Explicación:** Las ecuaciones despejadas son: x = (7 - y) / 3 y para la segunda: y = (6 - x) / 4. Observa cómo el nuevo valor de `x` se inyecta inmediatamente para calcular `y`.
* **A mano:** * Iteración 1: Iniciamos con x = 0.0, y = 0.0.
* Calcular x: x_nuevo = (7.0 - 0.0) / 3.0 = 2.3333.
* Calcular y (Uso del valor inmediato): y_nuevo = (6.0 - 2.3333) / 4.0 = 3.6667 / 4.0 = 0.9167.
* Fin de Iteración 1: Vector resultante = [2.3333, 0.9167]




* **Ejemplo 2: Segunda iteración del mismo sistema anterior**
* **Explicación:** Continuamos refinando los valores partiendo de la aproximación previa [2.3333, 0.9167].
* **A mano:** * Iteración 2: x_anterior = 2.3333, y_anterior = 0.9167.
* Calcular x: x_nuevo = (7.0 - 0.9167) / 3.0 = 6.0833 / 3.0 = 2.0278.
* Calcular y (Uso del valor inmediato): y_nuevo = (6.0 - 2.0278) / 4.0 = 3.9722 / 4.0 = 0.9931.
* Fin de Iteración 2: Vector aproximado = [2.0278, 0.9931] (Aproximándose velozmente a la solución real [2, 1]).




* **Ejemplo 3: Sistema diagonal estricto: (10x + y = 11), (2x + 10y = 12) con inicial [0,0]**
* **Explicación:** Fórmulas: x = (11 - y) / 10 | y = (12 - 2x) / 10.
* **A mano:** * Iteración 1:
* x_nuevo = (11.0 - 0.0) / 10.0 = 1.1000.
* y_nuevo = (12.0 - 2 * (1.1000)) / 10.0 = (12.0 - 2.2) / 10.0 = 9.8 / 10.0 = 0.9800.
* Resultado con 5 cifras significativas: [1.1000e+00, 9.8000e-01]





---

## 4. `Jacobi.py` (Método de Jacobi)

* **Definición:** Método iterativo para resolver sistemas de ecuaciones lineales. A diferencia de Gauss-Seidel, **no utiliza las variables recién calculadas dentro de la misma iteración**. En su lugar, todos los cálculos de la iteración actual se basan estrictamente en los valores que tenían las variables al terminar la iteración anterior (actualización simultánea en bloque).
* **Algoritmo (Lógica):**
1. Asegurar la dominancia diagonal de la matriz para garantizar la convergencia del proceso.
2. Despejar cada variable matemática de la diagonal en función de las demás incógnitas.
3. Guardar el estado inicial de las variables en un vector temporal de lectura.
4. Calcular el nuevo valor de cada incógnita utilizando **únicamente** los datos del vector temporal de la iteración anterior.
5. Una vez que se han calculado de forma independiente todos los nuevos valores de la iteración, actualizar el vector principal por completo (simultáneamente).
6. Repetir hasta cumplir la condición de tolerancia geométrica establecida.



### Código en Python

```python
import numpy as np

def jacobi(A, b, x0, tol=1e-5, max_iter=100):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x = np.array(x0, dtype=float)
    n = len(b)
    
    for k in range(max_iter):
        x_nuevo = np.zeros(n)
        
        for i in range(n):
            suma = 0.0
            for j in range(n):
                if i != j:
                    suma += A[i, j] * x[j] # Usa el 'x' fijo de la iteración anterior
            
            x_nuevo[i] = (b[i] - suma) / A[i, i]
            
        # Criterio de parada evaluando la diferencia antes del reemplazo total
        if np.max(abs(x_nuevo - x)) < tol:
            return x_nuevo
            
        # Reemplazo simultáneo al final del ciclo completo
        x = x_nuevo
    return x

# Ejemplo de ejecución
A_matriz = [[3.0, 1.0], [1.0, 4.0]]
b_vector = [7.0, 6.0]
x_inicio = [0.0, 0.0]
print("Solución Jacobi:", jacobi(A_matriz, b_vector, x_inicio))

```

### Explicación y Procedimiento a Mano

* **Ejemplo 1: Sistema: (3x + y = 7), (x + 4y = 6) con semilla inicial [0.0, 0.0]**
* **Explicación:** Las fórmulas de despeje son idénticas: x = (7 - y) / 3 y para la segunda: y = (6 - x) / 4. La diferencia crítica es que el cálculo de `y` no se ve afectado por el resultado de `x` de este mismo paso; ambos usan los ceros iniciales.
* **A mano:** * Iteración 1: Fijamos los valores base de lectura: x_ant = 0.0, y_ant = 0.0.
* Calcular x: x_nuevo = (7.0 - y_ant) / 3.0 = (7.0 - 0.0) / 3.0 = 2.3333.
* Calcular y (Uso del valor antiguo): y_nuevo = (6.0 - x_ant) / 4.0 = (6.0 - 0.0) / 4.0 = 1.5000.
* Actualización simultánea final: El nuevo vector pasa a ser [2.3333, 1.5000]




* **Ejemplo 2: Segunda iteración de Jacobi del mismo sistema**
* **Explicación:** Evaluamos el bloque completo usando los datos congelados del final del paso anterior: x_ant = 2.3333, y_ant = 1.5000.
* **A mano:** * Iteración 2:
* Calcular x: x_nuevo = (7.0 - y_ant) / 3.0 = (7.0 - 1.5000) / 3.0 = 5.5 / 3.0 = 1.8333.
* Calcular y: y_nuevo = (6.0 - x_ant) / 4.0 = (6.0 - 2.3333) / 4.0 = 3.6667 / 4.0 = 0.9167.
* Actualización simultánea final: El nuevo vector es [1.8333, 0.9167]. (Nota cómo avanza de forma distinta a Gauss-Seidel debido al desfase de actualización).




* **Ejemplo 3: Sistema diagonal estricto: (10x + y = 11), (2x + 10y = 12) con inicial [0,0]**
* **Explicación:** Fórmulas: x = (11 - y) / 10 | y = (12 - 2x) / 10.
* **A mano:** * Iteración 1: Usando x_ant = 0.0, y_ant = 0.0.
* x_nuevo = (11.0 - 0.0) / 10.0 = 1.1000.
* y_nuevo = (12.0 - 2 * (0.0)) / 10.0 = 12.0 / 10.0 = 1.2000.
* Reemplazo del bloque al cerrar el ciclo: [1.1000e+00, 1.2000e+00]
