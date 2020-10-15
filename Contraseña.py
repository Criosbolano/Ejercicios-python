def contrasena(password):

    validar=False #para validar qe se cumpla los requerimientos
    long=len(password) #para calcuar la longitud de la clave
    espacio=False #Valida espacios
    mayuscula=False #Valida letras mayusculas
    minuscula=False #Valida letras minusculas
    numeros=False #Variable para identificar numeros
    x=password.isalnum() #si es alfanumerica retorna true osea esta correcta
    correcto=True # si cumple los requerimientos todo esta correcto

    for variable in password: #ciclo que valida variable por variable

        if variable.isspace()==True: #Valida si la variable es un espacio
            espacio=True #si se encuentra un espacio
        if variable.isupper()==True: #Valida si hay mayusculas
            mayuscula=True #si se encuentra una mayuscula
        if variable.islower()==True: #Valida si hay minusculas
            minuscula=True #contador de minusculas
        if variable.isdigit()==True: #Valida si hay numeros
            numeros=True #contador de numeros

    if espacio==True: #si encuentra espacios
        print('La contraseña no puede tener espacios')
    else:
        validar=True #cumple con los requerimientos asi que continue

    if long < 8 and validar==True:
        print('minimo 8 caracteres')
        validar=False #es falso si no cumple con el requerimientos

    if mayuscula == True and minuscula == True and numeros == True and x== False and validar ==True:
        validar=True #que cumple requicito de tener mayu, min, numeros y no alfanumericos
    else:
        correcto=False#no cumple con uno o mas requerimientos

    if validar == True and correcto==False:
        print('contraseña no es segura: debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico')

    if validar == True and correcto ==True:
        return True

clave = input(' Escriba Contraseña: ')
print(contrasena(clave))
