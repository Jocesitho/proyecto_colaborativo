def fibonacci(n):
    secuencia = [0, 1]
    for i in range(2, n):
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
    return secuencia[:n]
# Modo de uso
cantidad = int(input("¿Cuántos números de Fibonacci quieres Sumar? "))
print(f"Los primeros {cantidad} números de Fibonacci son:")
print(fibonacci(cantidad))
