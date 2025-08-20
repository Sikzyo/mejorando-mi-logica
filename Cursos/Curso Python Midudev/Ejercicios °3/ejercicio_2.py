###
# Dada la siguiente lista:
# números = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
###

numbers = [10, 20, 30, 40, 50]

new_numbers = numbers[:]
new_numbers[0] = numbers[-1]
new_numbers[-1] = numbers[0]

print('Arreglo original', numbers)
print('Arreglo modificado', new_numbers)