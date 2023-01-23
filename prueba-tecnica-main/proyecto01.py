# Instrucciones

# Hacer un programa que juegue Piedra, papel o tijera, teniendo al usuario y
# la computadora como contrincantes

#################################################################################################

#Primero lo que tenia en mente era de tener una lista con valores. Despues queria que esos valores sean seleccionados aleatoriamente (a fin de simular una pc).
import random
#luego lei lo de este modulo para poder generar numero aleatorios pero lo use para elegir numeros aleatoriamente de la lista.

#Inicio del juego
#Crear un bucle y mientras sea verdadero que se ejecute el siguiente codigo
while True:
    #VARIABLES
    jugador_1 = int(input('Seleccione 1 = Piedra, 2 = Papel, 3 = Tijera')) #Seleccion del jugador
    jugador_pc = [1,2,3] #lista de numeros que simularan la computadora
    jugador_pc_eleccion = random.choice(jugador_pc) #eleccion aleatoria de los numeros que estan en la lista

    #CONDICIONALES, dependiendo de las elecciones tomadas tendremos los siguientes resultados.
    if jugador_1 == 1 and jugador_pc_eleccion == 2:
        print('Piedra pierde contra Papel')
    elif jugador_1 == 1 and jugador_pc_eleccion == 3:
        print('Piedra gana a Tijera')
    elif jugador_1 == 2 and jugador_pc_eleccion == 1:
        print('Papel gana contra Piedra')
    elif jugador_1 == 2 and jugador_pc_eleccion == 3:
        print('Papel pierde contra Tijera')
    elif jugador_1 == 3 and jugador_pc_eleccion == 1:
        print('Tijera pierde contra Piedra')
    elif jugador_1 == 3 and jugador_pc_eleccion == 2:
        print('Tijera gana a Papel')
    elif jugador_1 == jugador_pc_eleccion:
        print('Empate')

    #Si el usuario desea jugar otra vez.
    jugar_otra_vez = input('Escriba s para volver a jugar')
    if jugar_otra_vez != 's': #en caso que escriba una letra diferente a 's' se corta la ejecucion del juego.
        break

#Fin del juego