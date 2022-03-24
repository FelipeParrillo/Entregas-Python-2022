"""Necesitamos procesar las notas de los estudiantes de este curso. Queremos
saber:
• cuál es el promedio de las notas;
• cuántos estudiantes están por debajo del promedio"""
from re import X
from tkinter.tix import INTEGER


notas=[]
total=0
menor_promedio=0

aux=int(input('Ingresa la nota del siguiente alumno: '))
while aux!=-1:
    notas.append(aux)
    total=total+aux
    aux=int(input('Ingresa la nota del siguiente alumno: '))
promedio=(total/len(notas))    
print (f'La calificacion promedio es de : {promedio}' )

for i in range(len(notas)):
    if notas[i]<promedio:
        menor_promedio=menor_promedio+1
print(f'La cantidad de alumnos por debajo del promedio es: {menor_promedio}' )


