def cuenta_infinita(n):
    return cuenta_infinita(n + 1)

cuenta_infinita(1)
# Resultado: RecursionError: maximum recursion depth exceeded
