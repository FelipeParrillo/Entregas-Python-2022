""" Ingresar palabras desde el teclado hasta ingresar la palabra FIN. Imprimir
aquellas que empiecen y terminen con la misma letra.
• ¿Qué estructura de control deberíamos utilizar para realizar esta iteración? ¿Podemos utilizar
la sentencia for?
"""

palabra=input('Ingresa la palabra: ')
while palabra != 'FIN':
    if(palabra[0]==palabra[len(palabra)-1]):
        print(f'La palabra: {palabra} tiene la misma letra cuando comienza q cuando termina')
    palabra=input('Ingresa la palabra: ')

