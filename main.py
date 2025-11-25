def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Modo de uso
numero = int(input("Ingresa un número entero que deseas consultar: "))
if es_primo(numero):
    print(f"{numero} SI es un número primo.")
else:
    print(f"{numero} NO es un número primo.")
