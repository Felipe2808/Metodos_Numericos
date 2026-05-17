

# INTEGRACIÓN NUMÉRICA 

## 1. `Trapecio.py` (Método del Trapecio / Trapecio Compuesto)

* **Definición:** Método de integración numérica que aproxima el área bajo la curva de una función dividiendo el intervalo total en uno o varios subintervalos, reemplazando la curva real en cada segmento por una línea recta para formar trapecios y sumando sus áreas.
* **Algoritmo (Lógica):**
1. Definir los límites de integración [a, b] y el número de segmentos o subintervalos (n).
2. Calcular el ancho de cada base o paso: h = (b - a) / n.
3. Evaluar la función en los extremos: f(a) y f(b). Estos valores entran a la suma con peso 1.
4. Recorrer los puntos internos desde i = 1 hasta n - 1, calculando x_i = a + i * h, y evaluar f(x_i). Estos puntos internos entran a la suma con peso 2 (porque son compartidos por dos trapecios contiguos).
5. Aplicar la ecuación final: Integral = (h / 2) * [ f(a) + 2 * (Suma de f(x_i) internos) + f(b) ].



### Código en Python

```python
def f(x):
    # Función de ejemplo: x^2
    return x**2

def trapecio_compuesto(a, b, n):
    h = (b - a) / n
    
    # Suma de los extremos
    suma = f(a) + f(b)
    
    # Suma de los puntos internos (multiplicados por 2)
    for i in range(1, n):
        x_i = a + i * h
        suma += 2 * f(x_i)
        
    integral = (h / 2) * suma
    return integral

# Ejecución: Integral de x^2 desde 0 hasta 2 con 4 segmentos
print("Resultado Trapecio:", trapecio_compuesto(0, 2, 4))

```

### Explicación y Procedimiento a Mano

* **Ejemplo 1: f(x) = x^2 desde a = 0 hasta b = 2 con n = 2 segmentos**
* **Explicación:** El ancho de cada trapecio será h = (2 - 0) / 2 = 1.0. Los puntos a evaluar en el eje x serán: 0.0, 1.0 y 2.0.
* **A mano:** * Paso h = 1.0
* Evaluaciones: f(0) = 0^2 = 0.0 | f(1) = 1^2 = 1.0 | f(2) = 2^2 = 4.0
* Aplicando pesos: Suma = f(0) + 2 * f(1) + f(2) = 0.0 + 2 * (1.0) + 4.0 = 6.0
* Cálculo final: Integral = (1.0 / 2) * 6.0 = 3.0
* Resultado con 5 cifras significativas: 3.0000e+00




* **Ejemplo 2: f(x) = x^2 desde a = 0 hasta b = 2 con n = 4 segmentos**
* **Explicación:** Al aumentar los segmentos a 4, reducimos el error. El nuevo ancho es h = (2 - 0) / 4 = 0.5. Los puntos x serán: 0.0, 0.5, 1.0, 1.5, 2.0.
* **A mano:** * Paso h = 0.5
* Evaluaciones: f(0)=0.0, f(0.5)=0.25, f(1.0)=1.0, f(1.5)=2.25, f(2.0)=4.0
* Suma = 0.0 + 2 * (0.25 + 1.0 + 2.25) + 4.0 = 0.0 + 2 * (3.5) + 4.0 = 11.0
* Cálculo final: Integral = (0.5 / 2) * 11.0 = 0.25 * 11.0 = 2.75
* Resultado con 5 cifras significativas: 2.7500e+00 (Más cerca del valor real analítico que es 2.6667).




* **Ejemplo 3: f(x) = 1 / x desde a = 1 hasta b = 2 con n = 1 segmento (Trapecio Simple)**
* **Explicación:** Aplicamos la fórmula directa usando únicamente los dos extremos del intervalo. h = (2 - 1) / 1 = 1.0.
* **A mano:** * Evaluaciones: f(1) = 1 / 1 = 1.0 | f(2) = 1 / 2 = 0.5
* Suma directa de extremos = 1.0 + 0.5 = 1.5
* Cálculo final: Integral = (1.0 / 2) * 1.5 = 0.75
* Resultado con 5 cifras significativas: 7.5000e-01





---

## 2. `Simpson.py` (Reglas de Simpson 1/3 y 3/8 Compuestas)

* **Definición:** Métodos de integración numérica que ofrecen una precisión mucho mayor que el trapecio al aproximar el área bajo la curva mediante polinomios parábolicos (de segundo grado para Simpson 1/3) o cúbicos (de tercer grado para Simpson 3/8) conectados a través de grupos de puntos consecutivos.
* **Algoritmo (Lógica):**
* **Simpson 1/3:** Requiere obligatoriamente que el número de subintervalos (n) sea **par**. Calcula h = (b - a) / n. Los extremos llevan peso 1, los puntos con índice impar llevan peso 4 (polinomios internos) y los puntos internos con índice par llevan peso 2.
* Fórmula: Integral = (h / 3) * [ f(a) + 4 * (Suma Impares) + 2 * (Suma Pares) + f(b) ].


* **Simpson 3/8:** Requiere obligatoriamente que el número de subintervalos (n) sea **múltiplo de 3**. Calcula h = (b - a) / n. Los puntos internos que caen en posiciones múltiplos de 3 llevan peso 2, y el resto de los puntos internos llevan peso 3.
* Fórmula: Integral = (3 * h / 8) * [ f(a) + 3 * (Suma No Múltiplos de 3) + 2 * (Suma Múltiplos de 3) + f(b) ].





### Código en Python

```python
def f(x):
    return x**4  # Usaremos x^4 para notar la precisión de las reglas

def simpson_1_3(a, b, n):
    if n % 2 != 0:
        print("Error: n debe ser par para Simpson 1/3.")
        return None
    h = (b - a) / n
    suma = f(a) + f(b)
    
    for i in range(1, n):
        x_i = a + i * h
        if i % 2 != 0:
            suma += 4 * f(x_i)  # Índices impares
        else:
            suma += 2 * f(x_i)  # Índices pares
            
    return (h / 3) * suma

def simpson_3_8(a, b, n):
    if n % 3 != 0:
        print("Error: n debe ser múltiplo de 3 para Simpson 3/8.")
        return None
    h = (b - a) / n
    suma = f(a) + f(b)
    
    for i in range(1, n):
        x_i = a + i * h
        if i % 3 == 0:
            suma += 2 * f(x_i)  # Múltiplos de 3
        else:
            suma += 3 * f(x_i)  # No múltiplos de 3
            
    return (3 * h / 8) * suma

# Ejecución
print("Simpson 1/3 (n=4):", simpson_1_3(0, 2, 4))
print("Simpson 3/8 (n=3):", simpson_3_8(0, 2, 3))

```

### Explicación y Procedimiento a Mano

* **Ejemplo 1: Simpson 1/3 para f(x) = x^4 desde 0 hasta 2 con n = 2**
* **Explicación:** Evaluamos usando la parábola base. h = (2 - 0) / 2 = 1.0. Puntos: x0=0 (extremo), x1=1 (impar), x2=2 (extremo).
* **A mano:** * Evaluaciones: f(0)=0 | f(1)=1^4=1 | f(2)=2^4=16
* Estructura de pesos: Suma = f(0) + 4 * f(1) + f(2) = 0 + 4 * (1) + 16 = 20
* Cálculo: Integral = (1.0 / 3) * 20 = 6.6667
* Resultado con 5 cifras significativas: 6.6667e+00




* **Ejemplo 2: Simpson 1/3 para f(x) = x^4 desde 0 hasta 2 con n = 4**
* **Explicación:** h = (2 - 0) / 4 = 0.5. Índices impares: i=1 (x=0.5), i=3 (x=1.5). Índices pares internos: i=2 (x=1.0).
* **A mano:** * Evaluaciones: f(0)=0, f(0.5)=0.0625, f(1.0)=1.0, f(1.5)=5.0625, f(2.0)=16.0
* Suma = 0 + 4 * (0.0625 + 5.0625) + 2 * (1.0) + 16.0
* Suma = 0 + 4 * (5.125) + 2.0 + 16.0 = 0 + 20.5 + 2.0 + 16.0 = 38.5
* Cálculo: Integral = (0.5 / 3) * 38.5 = 6.4167
* Resultado con 5 cifras significativas: 6.4167e+00 (El valor exacto analítico es 6.4000).




* **Ejemplo 3: Simpson 3/8 para f(x) = x^4 desde 0 hasta 2 con n = 3**
* **Explicación:** Requiere n divisible por 3. h = (2 - 0) / 3 = 0.6667. Puntos: x0=0, x1=0.6667 (peso 3), x2=1.3333 (peso 3), x3=2 (extremo).
* **A mano:** * Evaluaciones: f(0)=0, f(0.6667)=0.1975, f(1.3333)=3.1605, f(2)=16.0
* Suma = 0 + 3 * (0.1975 + 3.1605) + 16.0 = 0 + 3 * (3.3580) + 16.0 = 10.074 + 16.0 = 26.074
* Cálculo: Integral = (3 * 0.6667 / 8) * 26.074 = (2.0 / 8) * 26.074 = 0.25 * 26.074 = 6.5185
* Resultado con 5 cifras significativas: 6.5185e+00





---

## 3. `CuadraturaGaussiana.py` (Método de la Cuadratura Gaussiana)

* **Definición:** Método de integración numérica de alta precisión que consiste en seleccionar estratégicamente tanto los puntos de evaluación (llamados nodos o raíces de Legendre) como sus respectivos coeficientes multiplicadores (pesos). A diferencia de los métodos anteriores que evalúan puntos espaciados uniformemente, la cuadratura gaussiana optimiza la ubicación de los puntos para integrar polinomios de grado 2n-1 de forma exacta utilizando sólo n puntos.
* **Algoritmo (Lógica):**
1. El método está definido originalmente de forma estricta para el intervalo [-1, 1].
2. Para cualquier intervalo general [a, b], aplicar un cambio de variable lineal para mapear los puntos `t` de [-1, 1] al dominio de `x` en [a, b] mediante: x = [ (b - a) * t + a + b ] / 2.
3. Calcular el diferencial de ajuste (Jacobiano): dx = [ (b - a) / 2 ] * dt.
4. Seleccionar el número de puntos de Gauss (n). Buscar en las tablas normalizadas los valores precalculados de los nodos (t_i) y sus pesos (w_i).
5. Evaluar la función en cada punto transformado x(t_i), multiplicarla por su respectivo peso w_i y acumular la suma.
6. Multiplicar el gran total de la suma por el factor de escala exterior: [ (b - a) / 2 ].



### Código en Python

```python
def f(x):
    return x**2

def cuadratura_gauss_2_puntos(a, b):
    # Tabla normalizada fija para n = 2 puntos en [-1, 1]
    # Nodos (raíces de Legendre)
    t1 = -0.5773502691896257  # corresponde a -1 / raiz_cuadrada(3)
    t2 = 0.5773502691896257   # corresponde a 1 / raiz_cuadrada(3)
    
    # Pesos asociados
    w1 = 1.0
    w2 = 1.0
    
    # Cambio de variable: mapear de t en [-1, 1] hacia x en [a, b]
    x1 = ((b - a) * t1 + a + b) / 2
    x2 = ((b - a) * t2 + a + b) / 2
    
    # Evaluación de la función con sus pesos correspondientes
    suma = w1 * f(x1) + w2 * f(x2)
    
    # Escalado por el Jacobiano del cambio de intervalo
    integral = ((b - a) / 2) * suma
    return integral

# Ejecución de prueba para x^2 desde 0 hasta 2
print("Resultado Cuadratura (2 pts):", cuadratura_gauss_2_puntos(0, 2))

```

### Explicación y Procedimiento a Mano

* **Ejemplo 1: f(x) = x^2 desde a = 0 hasta b = 2 usando n = 2 puntos de Gauss**
* **Explicación:** Realizamos el cambio de variable obligatorio desde el espacio [-1, 1] al espacio real [0, 2].
* **A mano:** * Factor exterior (Jacobiano) = (2 - 0) / 2 = 1.0
* Ecuación de transformación de puntos: x = [ 2 * t + 0 + 2 ] / 2 = t + 1
* Transformando Nodo 1: x1 = -0.5774 + 1 = 0.4226
* Transformando Nodo 2: x2 = 0.5774 + 1 = 1.5774
* Evaluaciones: f(0.4226) = (0.4226)^2 = 0.1786 | f(1.5774) = (1.5774)^2 = 2.4881
* Aplicando pesos (w=1): Suma = 1.0 * (0.1786) + 1.0 * (2.4881) = 2.6667
* Multiplicación final: Integral = 1.0 * 2.6667 = 2.6667
* Resultado con 5 cifras significativas: 2.6667e+00 (Da el valor exacto teórico de la integral con tan sólo dos evaluaciones).




* **Ejemplo 2: f(x) = x^3 desde a = 0 hasta b = 1 usando n = 2 puntos de Gauss**
* **Explicación:** Evaluamos un polinomio de tercer grado. La teoría promete precisión exacta para polinomios de grado hasta 2(2)-1 = 3 utilizando 2 puntos.
* **A mano:** * Factor exterior = (1 - 0) / 2 = 0.5
* Fórmula de mapeo: x = (1 * t + 1) / 2 = 0.5 * t + 0.5
* x1 = 0.5 * (-0.5774) + 0.5 = -0.2887 + 0.5 = 0.2113
* x2 = 0.5 * (0.5774) + 0.5 = 0.2887 + 0.5 = 0.7887
* Evaluaciones: f(0.2113) = 0.0094 | f(0.7887) = 0.4906
* Suma con pesos de 1.0 = 0.0094 + 0.4906 = 0.5000
* Final: Integral = 0.5 * (0.5000) = 0.2500
* Resultado con 5 cifras significativas: 2.5000e-01 (Idéntico a la solución analítica de integrar x^3).




* **Ejemplo 3: f(x) = 1 / x desde a = 1 hasta b = 2 usando n = 2 puntos de Gauss**
* **Explicación:** Probamos con una función no polinómica para observar la aproximación.
* **A mano:** * Factor exterior = (2 - 1) / 2 = 0.5
* Fórmula de mapeo: x = (1 * t + 3) / 2 = 0.5 * t + 1.5
* x1 = 0.5 * (-0.5774) + 1.5 = 1.2113
* x2 = 0.5 * (0.5774) + 1.5 = 1.7887
* Evaluaciones: f(1.2113) = 1 / 1.2113 = 0.8255 | f(1.7887) = 1 / 1.7887 = 0.5591
* Suma con pesos: 1.0 * (0.8255) + 1.0 * (0.5591) = 1.3846
* Multiplicación final: Integral = 0.5 * 1.3846 = 0.6923
* Resultado con 5 cifras significativas: 6.9230e-01 (El valor analítico exacto por logaritmo natural es 0.6931).
