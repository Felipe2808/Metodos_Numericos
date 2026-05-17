

# MÉTODOS NUMÉRICOS 

## 1. `Biseccion.py` (Método de Bisección)

* **Definición:** Método cerrado de búsqueda de raíces que divide repetidamente a la mitad un intervalo que contiene una raíz y selecciona el subintervalo donde la función cambia de signo. Es sumamente robusto y siempre converge si la función es continua en el intervalo dado.
* **Algoritmo (Lógica):**
1. Definir un intervalo inicial [a, b] tal que f(a) * f(b) < 0 (Teorema del Valor Intermedio).
2. Calcular el punto medio: c = (a + b) / 2.
3. Evaluar f(c). Si f(c) es aproximadamente 0 (o menor a la tolerancia), `c` es la raíz.
4. Si f(a) * f(c) < 0, la raíz está en el subintervalo izquierdo, por lo que el nuevo extremo derecho pasa a ser b = c.
5. De lo contrario, la raíz está en el derecho, por lo que a = c.
6. Repetir desde el paso 2 hasta cumplir el criterio de parada (tolerancia o iteraciones máximas).



### Código en Python

```python
def f(x):
    # Función de ejemplo: x^2 - 4
    return x**2 - 4

def biseccion(a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        print("El intervalo no encierra una raíz (f(a)*f(b) >= 0)")
        return None
    
    for i in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

# Ejecución
raiz = biseccion(0, 3)
print(f"Raíz encontrada: {raiz}")

```

### Explicación y Procedimiento a Mano

* **Ejemplo 1: f(x) = x^2 - 4 en el intervalo [0, 3]**
* **Explicación:** Buscamos el valor donde la parábola corta el eje x en la zona positiva. Evaluamos los signos en los extremos: f(0) = -4 (negativo) y f(3) = 5 (positivo). Como hay cambio de signo, el método puede iniciar.
* **A mano:** * Iteración 1: Intervalo = [0, 3] | Punto medio c = (0 + 3) / 2 = 1.5000
* Evaluar: f(1.5) = 1.5^2 - 4 = -1.7500.
* Decisión: Como f(1.5) es negativo y f(3) es positivo, la raíz está en el lado derecho.
* Nuevo Intervalo = [1.5000, 3.0000]




* **Ejemplo 2: f(x) = x^3 - x - 2 en el intervalo [1, 2]**
* **Explicación:** Evaluamos extremos para verificar el teorema: f(1) = -2 y f(2) = 4. Hay una raíz real garantizada entre 1 y 2.
* **A mano:** * Iteración 1: Intervalo = [1, 2] | Punto medio c = (1 + 2) / 2 = 1.5000
* Evaluar: f(1.5) = 1.5^3 - 1.5 - 2 = -0.1250.
* Decisión: f(1.5) es negativo, f(2) es positivo. La raíz se queda a la derecha.
* Nuevo Intervalo = [1.5000, 2.0000]




* **Ejemplo 3: f(x) = cos(x) - x en el intervalo [0, 1]**
* **Explicación:** Buscamos la intersección de la curva coseno con la recta de 45 grados. f(0) = 1.0 (positivo) y f(1) = cos(1) - 1 = -0.4597 (negativo).
* **A mano:** * Iteración 1: Intervalo = [0, 1] | Punto medio c = (0 + 1) / 2 = 0.5000
* Evaluar: f(0.5) = cos(0.5) - 0.5 = 0.8776 - 0.5 = 0.3776.
* Decisión: f(0.5) es positivo, f(1) es negativo. La raíz se queda a la derecha.
* Nuevo Intervalo = [0.5000, 1.0000]





---

## 2. `Newton-Raphson.py` (Método de Newton-Raphson)

* **Definición:** Método abierto de aproximación iterativa que utiliza el valor de la función y su primera derivada (la pendiente de la recta tangente) en un punto dado para predecir rápidamente dónde cruza el eje horizontal. Ofrece una velocidad de convergencia cuadrática, aunque requiere conocer la derivada analítica y una buena aproximación inicial.
* **Algoritmo (Lógica):**
1. Seleccionar un valor semilla o aproximación inicial x0.
2. Calcular el valor de la función f(x0) y su derivada df(x0).
3. Proyectar el cruce con el eje mediante la ecuación de actualización: x_nuevo = x0 - [ f(x0) / df(x0) ].
4. Si la derivada df(x0) es igual o muy cercana a 0, el método falla por división entre cero (recta tangente horizontal).
5. Si la diferencia entre x_nuevo y x0 es menor a la tolerancia, se detiene. De lo contrario, x0 = x_nuevo y se repite desde el paso 2.



### Código en Python

```python
def f(x):
    return x**2 - 4

def df(x):
    # Derivada analítica de f(x)
    return 2*x

def newton_raphson(x0, tol=1e-5, max_iter=100):
    x = x0
    for i in range(max_iter):
        derivada = df(x)
        if derivada == 0:
            print("Error: Derivada igual a cero.")
            return None
        
        x_nuevo = x - f(x) / derivada
        if abs(x_nuevo - x) < tol:
            return x_nuevo
        x = x_nuevo
    return x

# Ejecución
raiz = newton_raphson(x0=3.0)
print(f"Raíz encontrada: {raiz}")

```

### Explicación y Procedimiento a Mano

* **Ejemplo 1: f(x) = x^2 - 4 con x0 = 3.0**
* **Explicación:** Intentaremos aproximar la raíz x = 2 partiendo desde el valor 3. La derivada matemática de la función es f'(x) = 2x.
* **A mano:** * Iteración 1: x0 = 3.0000
* Evaluar: f(3.0) = 3^2 - 4 = 5.0000 | f'(3.0) = 2 * 3 = 6.0000
* Actualización: x1 = 3.0 - (5.0 / 6.0) = 3.0 - 0.8333 = 2.1667
* Resultado con 5 cifras significativas: 2.1667e+00




* **Ejemplo 2: f(x) = x^3 - x - 2 con x0 = 2.0**
* **Explicación:** Buscaremos la raíz de este polinomio partiendo desde x = 2. Su derivada corresponde a f'(x) = 3 * x^2 - 1.
* **A mano:** * Iteración 1: x0 = 2.0000
* Evaluar: f(2.0) = 2^3 - 2 - 2 = 4.0000 | f'(2.0) = 3 * (2^2) - 1 = 11.0000
* Actualización: x1 = 2.0 - (4.0 / 11.0) = 2.0 - 0.3636 = 1.6364
* Resultado con 5 cifras significativas: 1.6364e+00




* **Ejemplo 3: f(x) = cos(x) - x con x0 = 0.5**
* **Explicación:** Aproximamos el punto de equilibrio usando trigonometría básica. La derivada calculada analíticamente es f'(x) = -sin(x) - 1.
* **A mano:** * Iteración 1: x0 = 0.5000 (en radianes)
* Evaluar: f(0.5) = cos(0.5) - 0.5 = 0.3776
* Evaluar derivada: f'(0.5) = -sin(0.5) - 1 = -0.4794 - 1 = -1.4794
* Actualización: x1 = 0.5 - [0.3776 / (-1.4794)] = 0.5 + 0.2552 = 0.7552
* Resultado con 5 cifras significativas: 7.5522e-01





---

## 3. `ReglaFalsa.py` (Método de la Regla Falsa / Falsa Posición)

* **Definición:** Método cerrado que, a diferencia de la bisección, no divide el intervalo rígidamente por su punto medio geométrico. En su lugar, une los puntos extremos (a, f(a)) y (b, f(b)) con una línea recta secante y toma la intersección de esa recta con el eje x como la siguiente aproximación.
* **Algoritmo (Lógica):**
1. Definir un intervalo cerrado [a, b] que cumpla la condición f(a) * f(b) < 0.
2. Calcular el punto de cruce de la recta mediante la fórmula: c = b - [ f(b) * (a - b) ] / [ f(a) - f(b) ].
3. Evaluar f(c). Si el resultado cumple con los criterios de precisión exigidos, se asume como la raíz.
4. Analizar los signos: si f(a) * f(c) < 0, la raíz está en el tramo izquierdo, haciendo b = c.
5. Si no se cumple, la raíz está a la derecha, por lo que a = c.
6. Repetir la secuencia hasta converger.



### Código en Python

```python
def f(x):
    return x**2 - 4

def regla_falsa(a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        print("El intervalo no encierra una raíz.")
        return None
    
    c = a
    for i in range(max_iter):
        # Fórmula de interpolación lineal
        c_anterior = c
        c = b - (f(b) * (a - b)) / (f(a) - f(b))
        
        if abs(f(c)) < tol or abs(c - c_anterior) < tol:
            return c
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

# Ejecución
raiz = regla_falsa(0, 3)
print(f"Raíz encontrada: {raiz}")

```

### Explicación y Procedimiento a Mano

* **Ejemplo 1: f(x) = x^2 - 4 en el intervalo [0, 3]**
* **Explicación:** Unimos el punto inicial mínimo f(0) = -4 y el máximo f(3) = 5 para trazar la recta e inclinar la búsqueda hacia donde la curva ejerce más fuerza de atracción.
* **A mano:** * Iteración 1: a = 0.0, b = 3.0 | f(a) = -4.0, f(b) = 5.0
* Cálculo de c: c = 3.0 - [5.0 * (0.0 - 3.0)] / [-4.0 - 5.0]
* Desarrollo: c = 3.0 - [-15.0] / [-9.0] = 3.0 - 1.6667 = 1.3333
* Evaluar: f(1.3333) = (1.3333)^2 - 4 = -2.2222
* Decisión: Como f(0) * f(1.3333) > 0, cambiamos el extremo izquierdo: a = 1.3333
* Nuevo Intervalo = [1.3333, 3.0000]




* **Ejemplo 2: f(x) = x^3 - x - 2 en el intervalo [1, 2]**
* **Explicación:** Buscamos acelerar el proceso de acotamiento estimando proporciones lineales en lugar de simplemente partir el bloque a la mitad.
* **A mano:** * Iteración 1: a = 1.0, b = 2.0 | f(a) = -2.0, f(b) = 4.0
* Cálculo de c: c = 2.0 - [4.0 * (1.0 - 2.0)] / [-2.0 - 4.0]
* Desarrollo: c = 2.0 - [-4.0] / [-6.0] = 2.0 - 0.6667 = 1.3333
* Evaluar: f(1.3333) = (1.3333)^3 - 1.3333 - 2 = -0.9630
* Decisión: Como f(1.3333) es negativo, actualiza el límite inferior: a = 1.3333
* Nuevo Intervalo = [1.3333, 2.0000]




* **Ejemplo 3: f(x) = cos(x) - x en el intervalo [0, 1]**
* **Explicación:** Trazamos el segmento lineal que conecta los extremos trigonométricos f(0) = 1.0 y f(1) = -0.4597.
* **A mano:** * Iteración 1: a = 0.0, b = 1.0 | f(a) = 1.0, f(b) = -0.4597
* Cálculo de c: c = 1.0 - [(-0.4597) * (0.0 - 1.0)] / [1.0 - (-0.4597)]
* Desarrollo: c = 1.0 - [0.4597] / [1.4597] = 1.0 - 0.3149 = 0.6851
* Resultado con 5 cifras significativas en el punto estimado: 6.8510e-01





---

## 4. `Secante.py` (Método de la Secante)

* **Definición:** Método abierto que puede considerarse una variación de Newton-Raphson. Su gran ventaja radica en que **no requiere calcular la derivada analítica** de la función; en su lugar, aproxima la pendiente de la tangente utilizando una recta secante que pasa por dos puntos iterativos anteriores (x0 y x1).
* **Algoritmo (Lógica):**
1. Seleccionar dos aproximaciones iniciales cualesquiera, x0 y x1 (no es obligatorio que la raíz esté confinada entre ellos).
2. Calcular f(x0) y f(x1).
3. Proyectar la aproximación del siguiente punto (x2) mediante la pendiente sustituta: x2 = x1 - [ f(x1) * (x1 - x0) ] / [ f(x1) - f(x0) ].
4. Si el denominador [f(x1) - f(x0)] es igual a 0, el método se interrumpe por indeterminación física.
5. Validar convergencia: si la diferencia absoluta entre el nuevo punto y el anterior es menor que la tolerancia, terminar.
6. Reasignar variables para avanzar: x0 = x1, x1 = x2 y regresar al paso 2.



### Código en Python

```python
def f(x):
    return x**2 - 4

def secante(x0, x1, tol=1e-5, max_iter=100):
    for i in range(max_iter):
        denominador = f(x1) - f(x0)
        if denominador == 0:
            print("Error: Denominador igual a cero (Pendiente nula).")
            return None
        
        # Fórmula del método de la secante
        x2 = x1 - (f(x1) * (x1 - x0)) / denominador
        
        if abs(x2 - x1) < tol:
            return x2
        
        # Desplazamiento de los puntos
        x0 = x1
        x1 = x2
    return x1

# Ejecución utilizando dos semillas iniciales
raiz = secante(x0=3.0, x1=2.5)
print(f"Raíz encontrada: {raiz}")

```

### Explicación y Procedimiento a Mano

* **Ejemplo 1: f(x) = x^2 - 4 con x0 = 3.0 y x1 = 2.5**
* **Explicación:** Buscamos aproximar x = 2 sin conocer la derivada analítica. Usamos la información del comportamiento de la curva entre los puntos de prueba x = 3.0 y x = 2.5.
* **A mano:** * Datos iniciales: x0 = 3.0 (f(x0) = 5.0) | x1 = 2.5 (f(x1) = 2.25)
* Cálculo de x2: x2 = 2.5 - [2.25 * (2.5 - 3.0)] / [2.25 - 5.0]
* Desarrollo: x2 = 2.5 - [2.25 * (-0.5)] / [-2.75] = 2.5 - [ -1.125 ] / [ -2.75 ]
* Operación final: x2 = 2.5 - 0.4091 = 2.0909
* Siguiente paso preparado: El nuevo x0 será 2.5 y el nuevo x1 será 2.0909




* **Ejemplo 2: f(x) = x^3 - x - 2 con x0 = 1.0 y x1 = 2.0**
* **Explicación:** Proyectamos el crecimiento del polinomio basándonos en la diferencia de altura de sus valores f(1) y f(2).
* **A mano:** * Datos iniciales: x0 = 1.0 (f(x0) = -2.0) | x1 = 2.0 (f(x1) = 4.0)
* Denominador: f(2.0) - f(1.0) = 4.0 - (-2.0) = 6.0
* Cálculo de x2: x2 = 2.0 - [4.0 * (2.0 - 1.0)] / 6.0
* Desarrollo: x2 = 2.0 - [4.0 * 1.0] / 6.0 = 2.0 - 0.6667 = 1.3333
* Resultado con 5 cifras significativas: 1.3333e+00




* **Ejemplo 3: f(x) = cos(x) - x con x0 = 0.0 y x1 = 1.0**
* **Explicación:** Evaluamos el cambio de inclinación de la combinación trigonométrica en los extremos del cuadrante estándar.
* **A mano:** * Datos iniciales: x0 = 0.0 (f(x0) = 1.0) | x1 = 1.0 (f(x1) = -0.4597)
* Denominador: -0.4597 - 1.0 = -1.4597
* Cálculo de x2: x2 = 1.0 - [(-0.4597) * (1.0 - 0.0)] / [-1.4597]
* Desarrollo: x2 = 1.0 - [0.4597] / [-1.4597] = 1.0 - (-0.3149) = 0.6851
* Resultado con 5 cifras significativas antes del intercambio de variables: 6.8510e-01
