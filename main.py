import math
def es_primo(n):
    """Verifica si un número es primo"""
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

def verificar_primos():
    """Función para verificar si un número es primo"""
    while True:
        print("\n" + "-"*40)
        try:
            numero = int(input("Ingresa un número entero: "))
            
            if es_primo(numero):
                print(f"✓ {numero} SI es un número primo.")
            else:
                print(f"✗ {numero} NO es un número primo.")
            
            # Preguntar si desea continuar
            print("-"*40)
            continuar = input("¿Verificar otro número? (s/n): ").strip().lower()
            
            if continuar not in ['s', 'si', 'sí']:
                print("\nRegresando al menú principal...\n")
                break
                
        except ValueError:
            print("ERROR: Ingresa un número entero válido.")
        except KeyboardInterrupt:
            print("\n\nInterrumpido. Regresando al menú...\n")
            break

def menu_principal1():
    """Menú principal del programa"""
    while True:
        print("="*40)
        print("  VERIFICADOR DE NÚMEROS PRIMOS")
        print("="*40)
        print("1. Verificar números primos")
        print("2. Salir")
        print("="*40)
        
        opcion = input("Selecciona una opción (1-2): ").strip()
        
        if opcion == '1':
            verificar_primos()
        elif opcion == '2':
            print("\n¡Gracias por usar el programa!")
            print("Cerrando...\n")
            break
        else:
            print("\n⚠ Opción inválida. Elige 1 o 2.\n")

# Punto de entrada del programa
if __name__ == "__main__":
    try:
        menu_principal1()
    except KeyboardInterrupt:
        print("\n\nPrograma terminado por el usuario.\n")
        
def es_perfecto(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma == n

def generar_numeros_perfectos(n):
    encontrados = []
    numero = 2
    while len(encontrados) < n:
        if es_perfecto(numero):
            encontrados.append(numero)
        numero += 1
    return encontrados

# Bucle principal infinito
while True:
    try:
        cantidad = int(input("\n¿Cuántos números perfectos deseas generar? "))
        resultado = generar_numeros_perfectos(cantidad)

        print(f"\nLos primeros {cantidad} números perfectos son:")
        print(resultado)

    except ValueError:
        print("Por favor, ingresa un número entero válido.")
        continue  # vuelve a pedir la cantidad

    # Preguntar si desea continuar
    opcion = input("\n¿Deseas generar más números perfectos? (s/n): ").strip().lower()

    if opcion == "s":
        continue  # vuelve al inicio del bucle
    else:
        print("\nRegresando al menú principal...\n")
        break  # rompe el bucle y sale al menú principal (fin del programa)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def menu_fibonacci():
    while True:
        try:
            n = int(input("Ingrese la posición del número Fibonacci que desea calcular: "))
            resultado = fibonacci(n)
            print(f"El número Fibonacci en la posición {n} es: {resultado}")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue

        opcion = input("\n¿Desea calcular otro número Fibonacci? (s/n): ").strip().lower()
        if opcion != 's':
            print("Regresando al menú principal...\n")
            break

# Simulación del menú principal
def menu_principal():
    while True:
        print("=== MENÚ PRINCIPAL ===")
        print("1. Calcular número Fibonacci")
        print("2. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            menu_fibonacci()
        elif opcion == '2':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

# Ejecutar el menú principal
menu_principal()



def calcular_factorial():
    while True:
        print("\n--- CÁLCULO DE FACTORIAL ---")
        
        try:
            numero = int(input("Ingrese un número para calcular su factorial: "))
            
            if numero < 0:
                print("Error: No se puede calcular el factorial de un número negativo.")
            else:
                resultado = math.factorial(numero)
                print(f"El factorial de {numero} es {resultado}")
        
        except ValueError:
            print("Error: Por favor ingrese un número válido.")
        
        # Preguntar si desea continuar
        print("\n¿Qué desea hacer?")
        print("1. Calcular otro factorial")
        print("2. Volver al menú principal")
        
        opcion = input("Seleccione una opción (1-2): ")
        
        if opcion == "2":
            print("Volviendo al menú principal...")
            break
        elif opcion != "1":
            print("Opción no válida. Volviendo al menú principal...")
            break

def mostrar_menu():
    print("\n📋 MENU PRINCIPAL")
    print("SELECCIONA LA FUNCIÓN QUE DESEAS REALIZAR.")
    print("1. Cálculo de Fibonacci")
    print("2. Cálculo del factorial de un número")
    print("3. Determinar si un número es primo")
    print("4. Generar la serie de los primeros N números perfectos")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("👉 Ingresa tu opción: ")

        if opcion == "1":
            n = int(input("¿Cuántos números de Fibonacci deseas generar? "))
            print("Serie de Fibonacci:", generar_fibonacci(n))

        elif opcion == "2":
            n = int(input("Ingresa un número entero: "))
            print(f"El factorial de {n} es: {calcular_factorial()}")

        elif opcion == "3":
            n = int(input("Ingresa un número entero: "))
            print(f"{n} {'es' if es_primo(n) else 'no es'} primo.")

        elif opcion == "4":
            n = int(input("¿Cuántos números perfectos deseas generar? "))
            print("Números perfectos:", generar_numeros_perfectos(n))

        elif opcion == "5":
            print("👋 ¡Gracias por usar el programa! Hasta pronto.")
            break

        else:
            print("❌ Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()



