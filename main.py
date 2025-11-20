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