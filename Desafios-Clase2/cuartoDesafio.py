"""Necesitamos procesar las notas de los estudiantes de este curso. Queremos
saber:
• cuál es el promedio de las notas,
• qué estudiantes están por debajo del promedio."""

alumnos = {}
t = 0
nom = input('Ingresa el nombre del alumno: ')
while nom != 'FIN':
    nota = int(input(f'Ingresa la nota del alumno {nom}: '))
    alumnos[nom] = nota
    nom = input('Ingresa el nombre del proximo alumno: ')
    t = t+nota
print(f'El promedio es: {t/len(alumnos)}')

for i in alumnos:
    if alumnos[i] < (t/len(alumnos)):
        print(f'El alumno {i} tiene una nota por debajo del promedio')

a = 1
