###
# Clasifica una edad ingresada por el usuario en:
#
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
###

try:
    edad = int(input('Por favor ingresa tu edad:\n'))

    if (edad >= 65):
        print('La edad ingresada es de un "Adulto mayor"')
    elif (edad >= 18):
        print('La edad ingresada es de tipo "Adulto"')
    elif (edad >= 13):
        print('La edad ingresada es de tipo "Adolescente"')
    elif (edad >= 3):
        print('La edad ingresada es de tipo "Niño"')
    elif (edad >= 0):
        print('La edad ingresada es de tipo "Bebé"')
    else:
        print('La edad ingresada no es valida')

except ValueError:
    print('Error al ingresar la edad')

