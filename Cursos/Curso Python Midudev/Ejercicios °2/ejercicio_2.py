###
# Pide al usuario dos números y una operación (+, -, \*, /). Realiza la operación y muestra el resultado (maneja la división entre cero).
###
try:
    number_1 = float(input("Ingresa un numero para realizar una operación: "))
    operator = input("Ingresa un operador (+, -, *, /)")
    number_2 = float(input("Ingresa el segundo numero para realizar una operación: "))

    if operator == '+':
        print('Suma: ', number_1 + number_2)
    elif operator == '-':
        print('Resta: ', number_1 - number_2)
    elif operator == '*':
        print('Multiplicación: ', number_1 * number_2)
    elif operator == '/':
        print('División: ', number_1 / number_2)  # ← AHORA está dentro del try
    else:
        print('Operador incorrecto')
        
except ZeroDivisionError:   
    print('No se puede dividir por 0')
except ValueError:          
    print('Error con los números ingresados')