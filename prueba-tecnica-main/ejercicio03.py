# Instrucciones

#Crear una funcion para validación de nombres de usuarios.
#Dicha funcion deberá validar lo siguiente:

# - El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
# - El nombre de usuario debe ser alfanumérico.
# - Nombre de usuario con menos de 6 caracteres, retorna el mensaje 'El nombre de usuario debe contener al
# menos 6 caracteres'.
# - Nombre de usuario con más de 12 caracteres, retorna el mensaje 'El nombre de usuario no puede contener
# más de 12 caracteres'.
# - Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje 'El nombre de usuario
# puede contener solo letras y números'.
# - Nombre de usuario válido, retorna 'Correcto!'

########################################################################################

#Pedimos el nombre de usuario
nombre_usuario = input('Ingrese su usuario')

#Determinamos su longitud
longitud_nombre_usuario = len(nombre_usuario)

#Determinamos si es alfanumerico
tipo_nombre_usuario = nombre_usuario.isalnum()

#Creamos la funcion para validar el usario, tomando como parametros su longitud y su tipo
def validar_usuario(longitud, tipo):
    #Comparamos su tipo, si es alfanumerico comparamos la longitud (< a 6 y > a 12)
    if tipo == True:
        if longitud < 6:
            print('El nombre de usuario debe contener al menos 6 caracteres')
        elif longitud > 12:
            print('El nombre de usuario no puede contener más de 12 caracteres')
        else:
            #Si todo lo anterior no se cumple podemos ingresar
            print('Usuario Crorrecto')
    else:
        #Si no es un alfanumerico imprime lo siguiente.
        print('El nombre de usuario puede contener solo letras y números')

validar_usuario(longitud_nombre_usuario, tipo_nombre_usuario)
