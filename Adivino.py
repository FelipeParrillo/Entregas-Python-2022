import random

# Variables #
numero_aleatorio = random.randrange(101)

# Devuelve string indicando si aciertas o no el numero [0-100] <= 5 intentos
def Adivinar(num_aleatorio):
    intento = 1
    print("Tenés 5 intentos para adivinar un número entre 0 y 100")
    while (intento <= 5):    
        num_ingresado = int(input('Ingresa tu número: '))
        if num_ingresado == num_aleatorio:
            return(f'Ganaste! y necesitaste {intento} intentos!!!')
        else:
            print('Mmmm ... No.. ese número no es... Seguí intentando.')
            intento += 1
    return(f'\n Perdiste :(\n El número era: {num_aleatorio}')

#Main
print(Adivinar(numero_aleatorio))
