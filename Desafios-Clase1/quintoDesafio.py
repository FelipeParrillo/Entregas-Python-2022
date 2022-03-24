"""• Dadas dos cadenas ingresadas desde el teclado, imprimir aquella que tenga más caracteres"""

str1=input('Ingresa la primera cadena: ')
str2=input('Ingresa la segunda cadena: ')

if len(str1) == len(str2):
    print('Son cadenas del mismo largo')
else:
    print(f'{str1} es la cadena mas larga') if len(str1) > len(str2) else print(f'{str2} es la cadena mas larga')