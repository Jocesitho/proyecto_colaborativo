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