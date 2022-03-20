import random

# Variables #
numero_aleatorio = random.randrange(101)

# Devuelve si aciertas o no el numero [0-99] <= 5 intentos
def Adivinar(num_aleatorio):
    gane = False
    intento = 1
    print("Tenés 5 intentos para adivinar un número entre 0 y 100")
    while (intento <= 5 
           and not gane):    
        num_ingresado = int(input('Ingresa tu número: '))
        if num_ingresado == num_aleatorio:
            return('Ganaste! y necesitaste {} intentos!!!'.format(intento))
        else:
            print('Mmmm ... No.. ese número no es... Seguí intentando.')
            intento += 1
    if not gane:
        return('\n Perdiste :(\n El número era: {}'.format(num_aleatorio))

print(Adivinar(numero_aleatorio))
