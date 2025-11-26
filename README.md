Proyecto: Colaborativo de github

Este proyecto es un programa en Python que permite realizar operaciones matemáticas como verificar si un número es primo, generar números perfectos, calcular números Fibonacci y obtener factoriales. 
Incluye un menú interactivo para facilitar su uso desde la terminal.

| Integrante           | Rama asignada     |
| -------------------- | ----------------- |
| **Jose Arteaga**     | master            |
| **Habit Bermudez**   | feature-factorial |
| **Mauricio Herrera** | feature-fibonacci |
| **Jair Mendez**      | feature-primos    |
| **Juan Herrera**     | feature-perfectos |

Descripción del Programa
El programa ofrece un menú interactivo con las siguientes funciones:
1. Verificar si un número es primo
2. Generar los primeros N números perfectos
3. Calcular el número Fibonacci en una posición N
4. Calcular el factorial de un número
El menú permite repetir operaciones hasta que el usuario decida salir.

Diagrama de Flujo

             ┌──────────────┐
             │ Menú Principal│
             └───────┬──────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
  Verificar        Generar       Calcular
  primos           perfectos     Fibonacci/Factorial

Instrucciones de Ejecución
1. Requisitos
•	Python 3.x
2. Ejecutar el programa
1.	Guarda el archivo principal como main.py.
2.	Abre la terminal en la carpeta del proyecto.
3.	Ejecuta el comando: python main.py
4.	Usa el menú interactivo para elegir la operación que desees realizar.

Tecnologías utilizadas:
Python 3
Librería estándar math

Estructura del Proyecto:
/Proyecto-Matematicas
│
├── main.py
└── README.md

Notas:
Todas las operaciones son locales, no requieren conexión a internet.
El programa permite repetir las operaciones hasta salir.
