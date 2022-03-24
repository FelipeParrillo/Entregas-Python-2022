"""• Escribir un programa que ingrese 4 palabras desde el teclado e imprima aquellas que contienen
la letra “r”."""

# Dependiendo las precondiciones hay dos formas, en la primera q es necesario guardar los datos "palabras" en una estructura para luego imprimirlas todas juntas 
# y la segunda opcion que es ir informando a medida q se ingresan si tiene o no R

#1° Opcion:
lista=[]
for i in range (4):
    lista.append(input(f'Ingresa la palabra número {i + 1}: '))
for i in range(4):    
    if 'r' in (lista[i]):
        print(f'La palabra {lista[i]} lleva la letra "r"')
    else:
        print(f'La palabra {lista[i]} no tiene "r"')

#2° Opcion:
for i in range(4):
    if 'r' in (input(f'Ingresa la palabra número {i + 1}: ')):
        print('La palabra tiene "r"')
    else:
        print('La palabra no tiene "r"')