###
# Pide al usuario que introduzca dos números y muestra un mensaje indicando cuál es mayor o si son iguales.
###

print("Por favor ingresa un numero")
number_1 = int(input())

print("Por favor ingresa un segundo numero")
number_2 = int(input())

if number_1 > number_2:
    print(f"El numero {number_1} es mayor que {number_2}")
elif number_2 > number_1:
    print(f"El numero {number_2} es mayor que {number_1}")
else:
    print(f"Los números son iguales")