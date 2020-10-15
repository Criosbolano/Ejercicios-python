import Nombres_Usuarios
import Contraseña

correcto=False
while correcto==False:
    nombre=input('Digite nombre de usuario: ')
    if Nombres_Usuarios.apodo(nombre) ==True:
        print('Usuario registrado exitosamente')
        correcto=True

while correcto==True:
    clave=input('Ingrese contraseña: ')
    if Contraseña.contrasena(clave)==True:
        print('Contraseña creada exitosamente')
        correcto=False
