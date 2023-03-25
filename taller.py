import math

opcion = 0
while opcion != 7:
    print("")
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potenciación")
    print("6. Raíz cuadrada")
    print("7. Salir")
    print("")
    

    opcion = int(input())

    if opcion == 1:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 + num2
        print("El resultado de la suma es:", resultado)
    elif opcion == 2:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 - num2
        print("El resultado de la resta es:", resultado)
    elif opcion == 3:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 * num2
        print("El resultado de la multiplicación es:", resultado)
    elif opcion == 4:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        while num2 == 0:
            print("No se puede dividir entre cero. Inténtalo de nuevo.")
            num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
    elif opcion == 5:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 ** num2
        print("El resultado de la potenciación es:", resultado)
    elif opcion == 6:
        num = int(input("Ingresa un número entero positivo: "))
        while num < 0:
            print("El número debe ser entero positivo. Inténtalo de nuevo.")
            num = int(input("Ingresa un número entero positivo: "))
        resultado = math.sqrt(num)
        print("El resultado de la raíz cuadrada es:", resultado)
    elif opcion == 7:
        print("Fin de calculos!")
    else:
        print("Opción inválida. Por favor, elige una opción del 1 al 7.")