"""• Dado una letra ingresada por el teclado, queremos saber si es mayúscula o minúscula."""

mayusculas = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
minusculas = 'abcdefghijklmnñopqrstuvwxyz'
 
caracter = input('Ingrese una letra: ')
 
if caracter in mayusculas:
    print ('La letra es mayuscula')
elif caracter in minusculas:
    print ('La letra es minuscula')
else:
    print ('No es una letra')