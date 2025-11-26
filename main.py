import math

def es_primo(n):
    """Verifica si un número es primo."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def es_perfecto(n):
    """Determina si un número es perfecto."""
    suma = sum(i for i in range(1, n) if n % i == 0)
    return suma == n


def generar_numeros_perfectos(cantidad):
    """Genera los primeros N números perfectos."""
    encontrados = []
    num = 2
    while len(encontrados) < cantidad:
        if es_perfecto(num):
            encontrados.append(num)
        num += 1
    return encontrados


def fibonacci(n):
    """Calcula el número Fibonacci en la posición n."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def menu_primos():
    while True:
        print("\n--- VERIFICAR NÚMEROS PRIMOS ---")
        try:
            n = int(input("Ingresa un número entero: "))
            if es_primo(n):
                print(f"✓ {n} es primo.")
            else:
                print(f"✗ {n} NO es primo.")
        except ValueError:
            print("Ingresa un número válido.")
            continue

        if input("¿Deseas verificar otro? (s/n): ").lower() != "s":
            break


def menu_perfectos():
    while True:
        print("\n--- GENERAR NÚMEROS PERFECTOS ---")
        try:
            n = int(input("¿Cuántos números perfectos deseas generar?: "))
            print("Resultado:", generar_numeros_perfectos(n))
        except ValueError:
            print("Ingresa un número válido.")
            continue

        if input("¿Deseas generar otros? (s/n): ").lower() != "s":
            break


def menu_fibonacci():
    while True:
        print("\n--- NÚMEROS FIBONACCI ---")
        try:
            n = int(input("Ingresa la posición n: "))
            print(f"Fibonacci({n}) =", fibonacci(n))
        except ValueError:
            print("Ingresa un número válido.")
            continue

        if input("¿Deseas calcular otro? (s/n): ").lower() != "s":
            break


def menu_factorial():
    while True:
        print("\n--- CÁLCULO DE FACTORIAL ---")
        try:
            n = int(input("Ingresa un número entero: "))
            if n < 0:
                print("No existe factorial de números negativos.")
            else:
                print(f"{n}! =", math.factorial(n))
        except ValueError:
            print("Ingresa un número válido.")
            continue

        if input("¿Deseas calcular otro? (s/n): ").lower() != "s":
            break

def main():
    while True:
        print("\n===============================")
        print("        MENÚ PRINCIPAL")
        print("===============================")
        print("1. Verificar si un número es primo")
        print("2. Generar números perfectos")
        print("3. Calcular Fibonacci")
        print("4. Calcular factorial")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_primos()
        elif opcion == "2":
            menu_perfectos()
        elif opcion == "3":
            menu_fibonacci()
        elif opcion == "4":
            menu_factorial()
        elif opcion == "5":
            print("👋 Gracias por usar el programa.")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    main()




