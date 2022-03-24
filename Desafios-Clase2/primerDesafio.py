"""Vamos a modificar el código anterior para que se imprima la cadena “TIENE
R” si la palabra contiene la letra r y sino, imprima “NO TIENE R”.
"""
for x in range(4):
    str=input('Ingresa la cadena: ')
    print("TIENE R") if 'r' in (str) else print("NO TIENE R")
