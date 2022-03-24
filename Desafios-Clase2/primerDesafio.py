"""Vamos a modificar el código anterior para que se imprima la cadena “TIENE
R” si la palabra contiene la letra r y sino, imprima “NO TIENE R”.
"""
for i in range(4):
    cadena=input('Ingresa la cadena: ')
    print("TIENE R") if 'r' in (cadena) else print("NO TIENE R")
