"""• Dado un caracter ingresado por el teclado, queremos saber si es una comilla o no.
• ¿Hay algún problema?
"""

comillas=("\'\"")

car=(input('Ingrese un caracter: ')[:1])#solo toma el primer caracter

if car in (comillas):
    print('Es una comilla')
else:
    print('No es una comilla')