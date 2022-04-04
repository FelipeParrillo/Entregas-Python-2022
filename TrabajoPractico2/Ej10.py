"""Manipule estos archivos para realizar lo siguiente:
• Generar una estructura con los nombres de los estudiantes y la suma de ambas notas.
• Calcular el promedio de las notas totales e informar que alumnos obtuvieron menos que el
promedio.
"""


def crearEstructura():
    '''Retorna una lista con tuplas que tienen el nombre del alumno + la suma de sus dos notas'''
    with open("Python-Actividades\\Entregas-Python-2022\\TrabajoPractico2\\nombres_1.txt", encoding="utf8") as archivo_nombres:
        archN = archivo_nombres.read()
    with open("Python-Actividades\\Entregas-Python-2022\\TrabajoPractico2\\eval1.txt") as archivo_evaluacion1:
        archE1 = archivo_evaluacion1.read()
    with open("Python-Actividades\\Entregas-Python-2022\\TrabajoPractico2\\eval2.txt") as archivo_evaluacion2:
        archE2 = archivo_evaluacion2.read()

    nombres = archN.replace(",", "").replace("'", "").lower().split()
    eva1 = archE1.replace(",", "").split()
    eva2 = archE2.replace(",", "").split()

    # listaAlum Append en tuplas con el Nombre, Merge de las dos notas
    listaAlum = []
    for n in range(len(nombres)):
        nota = 0
        nota += int(eva1[n])
        nota += int(eva2[n])
        listaAlum.append((nombres[n], nota))

    archivo_nombres.close()
    archivo_evaluacion1.close()
    archivo_evaluacion2.close()
    return listaAlum


def promedio(listaA):
    '''Retorna el promedio de la lista pasada como parametro'''
    total = 0
    promedio = 0
    for n in range(len(listaA)):
        total = total + listaA[n][1]

    if total != 0:
        promedio = total/len(listaA)
    return promedio


def informar(listaA, prom):
    '''Retorna una lista de nombres que no superaron el prom'''
    lista = []
    for n in range(len(listaA)):
        if listaA[n][1] < prom:
            lista.append(listaA[n])
    return lista


listaA = crearEstructura()
print(
    f'El promedio de las notas es: {("{0:.2f}".format(promedio(listaA)))}\nLos alumnos que quedaron por debajo del promedio son: {informar(listaA,promedio(listaA))}')
