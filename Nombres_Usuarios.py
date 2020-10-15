import re

def apodo(nombre_usuario):

    x=nombre_usuario.isalnum()
    long=len(nombre_usuario)

    if x== False: #Si no contiene valores no alfanumericos
        print(' El nombre de usuario solo puede contener letras y números')

    if long < 6:
        print(' El nombre de usuario debe contener al menos 6 caracteres')

    if long > 12:
        print(" El nombre de usuario no puede contener más de 12 caracteres")

    if long > 5 and long < 13 and x==True:
        return ('Correcto usuario insertado') # es verdadero si el tamaño es mayor de a 5 y menor a 13

usuario = input(' Escriba Usuario: ')
print(apodo(usuario))
