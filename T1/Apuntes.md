

# REVISIÓN DE APUNTES (Versión apta para copiar y pegar)

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

```

### Explicación y Procedimiento a Mano

* **Ejemplo 1: len(12345.6)**
* **Explicación:** La función len() requiere un objeto contenedor (como un string, lista o tupla) para contar sus elementos mediante su puntero interno. Un flotante es un dato primitivo atómico sin longitud interna.
* **A mano:** * Objeto Evaluado = 12345.6 (Tipo: float)
* Condición de len(): ¿Tiene método __len__? -> FALSO.
* Resultado con 5 cifras significativas: No aplica (Error de Tipo)




* **Ejemplo 2: math.sqrt(-25.0)**
* **Explicación:** La raíz cuadrada en los números reales no está definida para valores negativos. El algoritmo de la librería estándar rechaza el valor de inmediato.
* **A mano:** * Función: f(x) = raíz_cuadrada(x), donde x debe ser mayor o igual a 0.
* Evaluando: x = -25.0 -> Como -25.0 < 0 (Está fuera del dominio real).
* Resultado con 5 cifras significativas: No aplica (Error de Valor)




* **Ejemplo 3: 50.0 / "2.5"**
* **Explicación:** Python es un lenguaje de tipado fuerte; no realiza una conversión automática (coerción) de cadenas de texto a números durante operaciones aritméticas binarias directas.
* **A mano:** * Operando A = 50.0 (float) / Operando B = "2.5" (string)
* Operación Binaria: float / string -> Operación no definida en el intérprete.
* Resultado con 5 cifras significativas: No aplica (Error de Tipo)





---

## 2. `Desbordamiento de Pila.py` (Stack Overflow / RecursionError)

* **Definición:** Agotamiento del espacio de memoria asignado a la pila de llamadas (Call Stack) debido a una sucesión excesiva de funciones anidadas que nunca liberan sus marcos de memoria.
* **Algoritmo (Lógica):**
1. Cada llamada a una función empuja (push) un registro de activación (variables locales, dirección de retorno) a la pila de llamadas.
2. Si la función es recursiva y carece de una condición de salida válida, la pila acumula marcos continuamente.
3. Al alcanzar el límite estricto impuesto por el intérprete (sys.getrecursionlimit()), el sistema interrumpe el proceso para evitar un colapso de la memoria del sistema operativo.



### Código en Python

```python
# Ejemplo 1: Recursión infinita directa
def bucle_infinito(n):
    return bucle_infinito(n + 1)

# Ejemplo 2: Factorial sin parada
def factorial_roto(n):
    return n * factorial_roto(n - 1)

# Ejemplo 3: Serie matemática acumulativa sin límite
def suma_infinita(n):
    return n + suma_infinita(n / 2)

```

### Explicación y Procedimiento a Mano

* **Ejemplo 1: bucle_infinito(1)**
* **Explicación:** Cada llamada genera una nueva instrucción idéntica que requiere una dirección de retorno en memoria, llenando la estructura lineal de la pila.
* **A mano:** * Pila de llamadas = [ f(1) -> f(2) -> f(3) -> ... -> f(1000) ]
* Límite por defecto en Python = 1000 llamadas.
* Llamada número 1001 -> Provoca el desbordamiento.
* Resultado con 5 cifras significativas del nivel de parada: 1.0000e+03 (es decir, 1000.0)




* **Ejemplo 2: factorial_roto(3)**
* **Explicación:** Al no comprobar si el número ha descendido a 1 o 0, la multiplicación aritmética se desplaza eternamente hacia los números negativos enteros.
* **A mano:** * Desarrollo: 3 * f(2) -> 3 * [2 * f(1)] -> 3 * 2 * [1 * f(0)] -> 3 * 2 * 1 * [0 * f(-1)] ...
* La cadena de evaluación nunca se cierra, manteniendo la memoria RAM retenida.
* Resultado de operaciones calculadas antes del colapso: Incomputable




* **Ejemplo 3: suma_infinita(10.0)**
* **Explicación:** Aunque matemáticamente la división sucesiva por 2 converge a valores infinitesimales, el número de funciones llamadas en el código sigue incrementándose linealmente de forma infinita.
* **A mano:** * Llamada 1: 10.0 + f(5.0)
* Llamada 2: 10.0 + [5.0 + f(2.5)]
* Llamada 3: 10.0 + 5.0 + [2.5 + f(1.25)] = 17.5
* La memoria física se agota por llamadas acumuladas antes de que el valor flotante llegue a cero absoluto.
* Resultado con 5 cifras significativas en la 3ra iteración: 1.7500e+01 (es decir, 17.500)





---

## 3. `MemoryError.py`

* **Definición:** Error crítico que ocurre cuando el programa solicita al Administrador de Memoria (Heap) una asignación de bytes para un objeto que supera la memoria física o virtual disponible en el sistema.
* **Algoritmo (Lógica):**
1. El script solicita la construcción de una estructura indexada (matrices, listas masivas).
2. El intérprete calcula los bytes requeridos basándose en el tipo de objeto.
3. Solicita el direccionamiento al sistema operativo.
4. Si el sistema operativo deniega la petición por falta de espacio libre, el proceso lanza la excepción para evitar corromper otros procesos activos.



### Código en Python

```python
# Ejemplo 1: Inicialización de matriz masiva
try:
    lista_gigante = [0] * (10**11)
except MemoryError:
    print("Error 1: Memoria RAM insuficiente para la lista.")

# Ejemplo 2: Duplicación exponencial de strings en bucle
try:
    cadena = "A"
    while True:
        cadena = cadena * 2
except MemoryError:
    print("Error 2: Agotamiento de Heap por crecimiento exponencial.")

# Ejemplo 3: Carga de un bloque masivo de flotantes desnudos
# (Mil millones de datos de alta precisión en un arreglo)

```

### Explicación y Procedimiento a Mano

* **Ejemplo 1: [0] * (1011)**
* **Explicación:** Cada número entero estructurado en Python consume un mínimo de 28 bytes de memoria física para sus metadatos internos.
* **A mano:** * Elementos solicitados = 10^11 (cien mil millones de enteros)
* Memoria requerida = (10^11) * 28 bytes = 2.8000e+12 bytes
* Conversión a Gigabytes = 2.8000e+12 / 10^9 = 2800.0 Gigabytes de RAM.
* Comparación: 2800.0 GB >> 16.000 GB (RAM promedio de PC) -> MemoryError




* **Ejemplo 2: cadena * 2 (Bucle Exponencial)**
* **Explicación:** Al duplicar el string en cada ciclo, el crecimiento de consumo de memoria se rige bajo la función matemática de potencia de 2 (2^n).
* **A mano:** * Iteración 0 = 1 byte | Iteración 10 = 1024 bytes
* Iteración 30 = 2^30 bytes = 1.0737e+09 bytes (Aprox 1 GB)
* Iteración 34 = 2^34 bytes = 1.7180e+10 bytes (Aprox 17.18 GB) -> Rompe una RAM de 16GB.




* **Ejemplo 3: Matriz simulada de 109 flotantes de doble precisión**
* **Explicación:** Guardar mil millones de flotantes puros (8 bytes por flotante de precisión doble) satura el direccionamiento continuo de la memoria del sistema.
* **A mano:** * Datos = 1,000,000,000 elementos.
* Memoria pura requería = 10^9 * 8 bytes = 8.0000e+09 bytes.
* Conversión exacta a Gigabytes = 8.0000 Gigabytes limpios de RAM (sin contar la estructura del script).





---

## 4. `Mutacióndelista.py` (RuntimeError o Errores de Desfase de Índice)

* **Definición:** Falla de consistencia lógica o de ejecución que se genera al alterar la estructura (longitud, posiciones) de una colección mientras un iterador activo la está recorriendo secuencialmente.
* **Algoritmo (Lógica):**
1. Un bucle establece un puntero de lectura interno que se incrementa en una unidad por cada paso (i = 0, 1, 2...).
2. Si el código interno elimina un elemento anterior a la posición actual, todos los elementos subsecuentes se desplazan a la izquierda.
3. El iterador avanza ciegamente al siguiente índice matemático, provocando que se salten datos o se consulte un índice que ya no existe en el nuevo tamaño reducido de la colección.



### Código en Python

```python
# Ejemplo 1: Mutación de diccionarios (Garantiza ruptura de ejecución)
try:
    dicc = {'x': 1, 'y': 2, 'z': 3}
    for clave in dicc:
        if clave == 'y':
            del dicc['y']
except RuntimeError as e:
    print(f"Error 1: {e}")

# Ejemplo 2: Desfase físico de índices en listas (IndexError)
try:
    valores = [10, 20, 30, 40]
    limite = len(valores)
    for i in range(limite):
        if valores[i] == 20:
            valores.pop(i)
except IndexError as e:
    print(f"Error 2: {e}")

# Ejemplo 3: Bucle infinito por adición descontrolada

```

### Explicación y Procedimiento a Mano

* **Ejemplo 1: Mutación de dicc**
* **Explicación:** Los diccionarios evalúan internamente una tabla Hash. Modificar las claves destruye la integridad del recorrido del iterador, lanzando un bloqueo de protección nativo de Python.
* **A mano:** * Longitud Inicial = 3.0000
* En el paso 'y' -> Se borra la clave 'y' -> Nueva Longitud = 2.0000
* Validación interna del bucle: Longitud anterior (3.0000) != Longitud actual (2.0000) -> RuntimeError.




* **Ejemplo 2: Desfase en valores.pop(i)**
* **Explicación:** El bucle ejecuta un rango fijo basado en el tamaño inicial (4). Al encoger la lista, los índices finales quedan vacíos, pero el bucle intenta leerlos obligatoriamente.
* **A mano:** * Inicio: Lista = [10, 20, 30, 40], Índices planificados a recorrer = 0, 1, 2, 3
* Ciclo i=1: El elemento es 20 -> Se ejecuta pop(1)
* Nueva Lista = [10, 30, 40], Nuevos Índices reales válidos = 0, 1, 2
* Ciclo i=3: El bucle intenta evaluar Lista[3] -> No existe -> IndexError.
* Resultado de la longitud final con 5 cifras significativas si el script controlara el error: 3.0000e+00




* **Ejemplo 3: Adición infinita en listas**
* **Explicación:** Si en lugar de borrar, añades elementos en cada ciclo, la condición de fin del bucle se desplaza hacia adelante más rápido de lo que el iterador avanza, provocando un ciclo infinito.
* **A mano:** * Lista inicial = [1, 2] (Longitud = 2)
* Paso i=0: Lee primer dato -> Añade un elemento nuevo -> Nueva Longitud = 3
* Paso i=1: Lee segundo dato -> Añade otro elemento nuevo -> Nueva Longitud = 4
* La diferencia (Longitud - Índice) siempre aumenta, el bucle jamás alcanza el final.
* Razón de crecimiento: 1.0000e+00 elemento por ciclo.





---

## 5. `OverflowError.py`

* **Definición:** Excepción matemática provocada cuando una operación aritmética con números decimales genera un valor de punto flotante que excede la capacidad de representación binaria máxima del estándar de hardware.
* **Algoritmo (Lógica):**
1. Python procesa operaciones de números decimales de doble precisión mediante el estándar IEEE 754.
2. Este estándar asigna 64 bits por número: 1 bit de signo, 11 bits para el exponente y 52 bits para la mantisa.
3. El número máximo absoluto almacenable matemáticamente es 1.7976931348623157e+308.
4. Si un resultado multiplica, eleva o convierte un número más allá de este límite, la ALU del procesador reporta un desbordamiento numérico superior.



### Código en Python

```python
import math
import sys

# Ejemplo 1: Límite máximo de la función exponencial flotante
try:
    # Justo en el límite permitido
    valor_valido = math.exp(709.78)
    print(f"Límite flotante calculado: {valor_valido:.4e}")
    # Rompiendo el límite
    resultado_1 = math.exp(710.0)
except OverflowError as e:
    print(f"Error 1: {e}")

# Ejemplo 2: Potencia directa sobrepasando la barrera IEEE 754
try:
    resultado_2 = 2.0 ** 1024
except OverflowError as e:
    print(f"Error 2: {e}")

# Ejemplo 3: Forzar conversión de entero masivo a tipo flotante
try:
    entero_grande = 10 ** 310
    resultado_3 = float(entero_grande)
except OverflowError as e:
    print(f"Error 3: {e}")

```

### Explicación y Procedimiento a Mano

* **Ejemplo 1: math.exp(710.0)**
* **Explicación:** La constante de Euler es e = 2.71828. Elevarla a la potencia 710 genera un número cuyo exponente en base 10 supera por completo los 308 órdenes de magnitud que tolera el hardware.
* **A mano:** * Cálculo al límite permisible: e^(709.7827)
* Valor aproximado: e^(709.7827) = 1.79769e+308 (Valor máximo del flotante)
* Para la instrucción e^(710.0): Como 710.0 > 709.7827 -> Provoca OverflowError.
* Resultado límite del sistema con 5 cifras significativas: 1.7977e+308




* **Ejemplo 2: 2.0  1024**
* **Explicación:** En el sistema binario puro de 64 bits, el exponente máximo es 2^1023. Intentar desplazar los bits del exponente al valor de 1024 satura los 11 bits asignados a dicha tarea en el procesador.
* **A mano:** * Último valor binario almacenable: 2^1023
* Operación analítica: 2^1023 = 8.9884656...e+307
* Resultado antes del colapso con 5 cifras significativas: 8.9885e+307
* Para 2^1024: El exponente desborda los 11 bits físicos disponibles -> OverflowError.




* **Ejemplo 3: float(10  310)**
* **Explicación:** Los enteros en Python se gestionan por software, por lo que pueden tener un tamaño ilimitado. Sin embargo, al intentar forzar su transformación a decimal (float), el número tiene que someterse a la regla física del hardware (máximo 10^308).
* **A mano:** * Restricción del hardware decimal: Número máximo = 1.7977e+308
* Evaluación: El entero ingresado es 10^310. Como 10^310 > 1.7977e+308 -> Provoca OverflowError.
* Diferencia de exceso evaluada con 5 cifras significativas: 1.0000e+310
    
