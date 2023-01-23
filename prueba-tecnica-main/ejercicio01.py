# Instrucciones

# Los estudiantes consultan la nota que recibirán según las calificaciones que obtuvieron

# Por ejemplo:

# Las calificaciones 4, 5, 3. Darán la nota 4
# Las calificaciones 3, 2, 5. Darán la nota 3.33

# Escribe algún código para determinar la nota de un estudiante

###############################################################################################3

#REGISTRO DE CALIFICACIONES.
#PEDIR AL ALUMNO QUE INGRESE SUS CALIFICACIONES.
primera_calificacion = int(input('Registre su calificación del primer examen'))
segunda_calificacion = int(input('Registre su calificación del segundo examen'))
tercera_calificacion = int(input('Registre su calificación del tercer examen'))


#FUNCIÓN QUE DETERMINA LA NOTA FINAL SEGÚN LAS CALIFICACIONES OBTENIDAS.
def nota_final(primera_etapa, segunda_etapa, tercera_etapa):
    promedio = (primera_etapa + segunda_etapa + tercera_etapa) / 3
    return promedio

nota_final(primera_calificacion, segunda_calificacion, tercera_calificacion)
