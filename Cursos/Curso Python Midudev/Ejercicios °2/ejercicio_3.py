###
# Pide al usuario que introduzca un año y determina si es bisiesto:
#
# Es divisible por 4.
# Excepto si es divisible por 100, pero no por 400.
###

try:
    year = int(input('Ingresa un año: '))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print('Si es bisiesto')
    else:
        print('No es bisiesto')
    
except:
    print('Error al introducir el año')