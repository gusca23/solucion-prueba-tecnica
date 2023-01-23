# Instrucciones

# Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase, seguido
# del porcentaje de veces que aparecela frase y el **porcentaje** de veces que aparece
# la letra en la frase.

########################################################################################

#PETICIÓN DE FRASE
frase_usuario = input('Escriba una frase')
#FRASE RECOMENDADA: Es mejor cojear por el camino que avanzar a grandes pasos fuera de él. Pues quien cojea en el camino, aunque avance poco, se acerca a la meta, mientras que quien va fuera de él, cuanto más corre, más se aleja.

#PETICIÓN DE LETRA
letra_usuario = input('Escoja una letra dentro de la frase.')

#ITERAR FRASE PARA DETERMINAR LAS VECES QUE APARECE LA LETRA EN LA FRASE CON LA AYUDA DE UN CONTADOR.
contador = 0

for letra_buscada in frase_usuario:
    if letra_buscada == letra_usuario:
        #Si se cumple la condicion ir adicionando para determinar la cantidad de veces que aparece dicha letra.
        contador = contador + 1
        #Una vez que se tenga la cantidad total de la letra, hallar su % con la siguiente regla de tres.
        #len(frase_usuario) : contador :: 100 : X 
        porcentaje = (contador * 100)//len(frase_usuario)

print(f"la letra elegida ({letra_usuario}) aparece {contador} veces que equivale al ({porcentaje}%) en la frase: {frase_usuario}")
