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

import math

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
            print("Números perfectos:", generar_numeros_perfectos())

        elif opcion == "5":
            print("👋 ¡Gracias por usar el programa! Hasta pronto.")
            break

        else:
            print("❌ Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()

