# Instrucciones

# Un número Armstrong es un número que es la suma de sus propios dígitos
# elevados cada uno a la potencia de la cantidad de dígitos.


# Por ejemplo:

#     9 es un número de Armstrong, porque 9 = 9^1 = 9
#     10 no es un número de Armstrong, porque 10 != 1^2 + 0^2 = 1
#     153 es un número de Armstrong, porque 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
#     154 no es un número de Armstrong, porque: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190

# Escribe algún código para determinar si un número es un número Armstrong.

#################################################################################################################

#Pedimos al usuario que ingrese un numero
numero = input('Escriba un número')

#Determinamos la cantidad de digitos de dicho numero
cantidad_digitos = len(numero)

#Inicializamos un contador en 0 para ir realizando la suma de las unidades
suma_unidades = 0

#Recorremos el numero para obtener cada unidad
for unidad in numero:
    #Sumamos cada unidad elevada a la potencia segun la cantidad de digitos
    suma_unidades = suma_unidades + (int(unidad)**len(numero))

#Comparamos los resultados:
if suma_unidades == int(numero):
    #Si son iguales imprimir que dicho numero es un numero Armstrong
    print(f'{numero} es un número Armstrong')
else:
    #Si no imprimir que dicho numero no es un nro Armstrong
    print(f'{numero} no es un número Armstrong')