###
# Dada la siguiente lista:
# 
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# 
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
###


try:
    mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
    secreto= mensaje[7:]
    print(secreto)
except:
    print('Error en la ejecución')