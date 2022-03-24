"""Vamos a modificar el código anterior para que se imprima la cadena “TIENE
R” si la palabra contiene la letra r y sino, imprima “NO TIENE R”.
"""

#Siempre intento programarlo a mi manera, pero este desafio me quedo igual al mostrado como solucion en el PDF Clase 2
# y creo q es la manera mas correcta de realizar el enunciado 
for x in range(4):
    str=input('Ingresa la cadena: ')
    print("TIENE R") if 'r' in (str) else print("NO TIENE R")
