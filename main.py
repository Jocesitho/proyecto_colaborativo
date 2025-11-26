
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
            print(f"El factorial de {n} es: {calcular_factorial(n)}")

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
