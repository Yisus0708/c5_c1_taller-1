#Ejercicio #2

saldo = 1000

print("Banco python")
print(f"Saldo inicial: ${saldo}")

operaciones = int(input("¿Cuántas operaciones desea realizar?: "))

for i in range(operaciones):
    print ("Menu UwU")
    print("1 → Consultar saldo")
    print("2 → Retirar dinero")
    print("3 → Depositar dinero")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        print(f"Saldo actual: ${saldo}")

    elif opcion == "2":
        monto = float(input("Ingrese el monto a retirar: "))

        while monto < 0:
            print("Error: el monto no puede ser negativo ):v")
            monto = float(input("Ingrese nuevamente el monto: "))

        if monto > saldo:
            print("Fondos insuficientes :(")
        else:
            saldo -= monto
            print("Retiro exitoso")
            print(f"Saldo actual: ${saldo}")

    elif opcion == "3":
        monto = float(input("Ingrese el monto a depositar: "))

        while monto < 0:
            print("Error: el monto no puede ser negativo ):v")
            monto = float(input("Ingrese nuevamente el monto: "))

        saldo += monto
        print("Depósito exitoso :D")
        print(f"Saldo actual: ${saldo}")

    else:
        print("Opción inválida")

print("\nGracias :D")