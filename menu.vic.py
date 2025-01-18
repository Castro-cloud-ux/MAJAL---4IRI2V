import math

def menu():
    print("\n--- Menú de Opciones ---")
    print("1. Suma de 'n' números")
    print("2. Producto entre 'n' números")
    print("3. División entre 2 números")
    print("4. Calcular el factorial de un número")
    print("5. Tablas de multiplicar del 1 al 10")
    print("6. Calcular el cuadrado y el cubo de un número")
    print("7. Promedio, máximo y mínimo de una serie de números")
    print("8. Salir")

def suma_numeros():
    numeros = []
    while True:
        try:
            num = int(input("Introduce un número (o -1 para terminar): "))
            if num == -1:
                break
            numeros.append(num)
        except ValueError:
            print("Por favor, introduce un número válido.")
    if numeros:
        print(f"La suma de los números es: {sum(numeros)}")
    else:
        print("No se introdujeron números.")

def producto_numeros():
    numeros = []
    while True:
        try:
            num = int(input("Introduce un número (o -1 para terminar): "))
            if num == -1:
                break
            numeros.append(num)
        except ValueError:
            print("Por favor, introduce un número válido.")
    if numeros:
        producto = 1
        for n in numeros:
            producto *= n
        print(f"El producto de los números es: {producto}")
    else:
        print("No se introdujeron números.")

def division():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        if num2 == 0:
            print("Error: No se puede dividir entre 0.")
        else:
            print(f"La división es: {num1 / num2}")
    except ValueError:
        print("Por favor, introduce números válidos.")

def factorial():
    try:
        num = int(input("Introduce un número entero positivo: "))
        if num < 0:
            print("El factorial no está definido para números negativos.")
        else:
            print(f"El factorial de {num} es: {math.factorial(num)}")
    except ValueError:
        print("Por favor, introduce un número entero.")

def tablas_multiplicar():
    try:
        num = int(input("Introduce el número para la tabla de multiplicar: "))
        print(f"Tabla de multiplicar del {num}:")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    except ValueError:
        print("Por favor, introduce un número entero.")

def cuadrado_cubo():
    try:
        num = float(input("Introduce un número: "))
        print(f"El cuadrado de {num} es: {num ** 2}")
        print(f"El cubo de {num} es: {num ** 3}")
    except ValueError:
        print("Por favor, introduce un número válido.")

def promedio_max_min():
    numeros = []
    while True:
        try:
            num = int(input("Introduce un número (o -1 para terminar): "))
            if num == -1:
                break
            numeros.append(num)
        except ValueError:
            print("Por favor, introduce un número válido.")
    if numeros:
        print(f"El promedio es: {sum(numeros) / len(numeros)}")
        print(f"El valor máximo es: {max(numeros)}")
        print(f"El valor mínimo es: {min(numeros)}")
        print(f"Total de números introducidos: {len(numeros)}")
    else:
        print("No se introdujeron números.")

def main():
    while True:
        menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            suma_numeros()
        elif opcion == "2":
            producto_numeros()
        elif opcion == "3":
            division()
        elif opcion == "4":
            factorial()
        elif opcion == "5":
            tablas_multiplicar()
        elif opcion == "6":
            cuadrado_cubo()
        elif opcion == "7":
            promedio_max_min()
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
