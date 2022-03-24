"""• Escribir un programa que ingrese desde teclado una cadena de caracteres e imprima cuántas
letras “a” contiene"""

str=input('Ingresa la cadena: ')
cant=0

for i in range(len(str)):
    if (str[i]=='a'):
        cant+=1
        
print(f'la cadena: {str} tiene {cant} letras "a" ')