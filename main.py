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