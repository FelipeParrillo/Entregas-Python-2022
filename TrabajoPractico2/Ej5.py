"""Dada una frase y un string ingresados por teclado (en ese orden), e informe la cantidad de
veces que se encuentra el string en la frase. No distingir entre mayúsculas y minúsculas."""

frase = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres"
palabra = input('Ingrese la plabra: ')

# 1° lo bajo a minusculas, 2°aun siendo string le remplazo las comas por vacio y 3° lo convierto en lista con el split()
frase = frase.lower().replace(',', "").split()
print(frase)
print(frase.count(palabra))
