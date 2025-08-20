###
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing. Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30.
###

lista = [10, 20, 30, 40, 50, 60, 70, 80, 90]

longitud_array = int((len(lista))/2)
print(lista[longitud_array])