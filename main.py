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

def menu_principal():
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
        menu_principal()
    except KeyboardInterrupt:
        print("\n\nPrograma terminado por el usuario.\n")