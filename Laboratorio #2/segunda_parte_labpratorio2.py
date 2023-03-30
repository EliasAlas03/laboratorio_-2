num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

print ("Determinar el número más grande")
if num1 > num2 and num1 > num3:
    print("El número", num1, "es el número más grande de los tres.")
elif num2 > num1 and num2 > num3:
    print("El número", num2, "es el número más grande de los tres.")
else:
    print("El número", num3, "es el número más grande de los tres.")

print("Determinar el número más pequeño")
if num1 < num2 and num1 < num3:
    print("El número", num1, "es el número más pequeño de los tres.")
elif num2 < num1 and num2 < num3:
    print("El número", num2, "es el número más pequeño de los tres.")
else:
    print("El número", num3, "es el número más pequeño de los tres.")

print ("Determinar el número de en medio")
if num1 < num2 and num1 > num3 or num1 > num2 and num1 < num3:
    print("El número", num1, "es el número de en medio de los tres.")
elif num2 < num1 and num2 > num3 or num2 > num1 and num2 < num3:
    print("El número", num2, "es el número de en medio de los tres.")
else:
    print("El número", num3, "es el número de en medio de los tres.")