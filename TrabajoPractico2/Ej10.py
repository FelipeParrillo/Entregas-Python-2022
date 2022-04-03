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
    pos = 0
    for n in nombres:
        nota = 0
        nota = nota + int(eva1[pos])
        nota = nota + int(eva2[pos])
        listaAlum.append((n, nota))
        pos += 1
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
prom = promedio(listaA)
listaB = informar(listaA, prom)
print(
    f'El promedio de las notas es: {prom}\n y los alumnos que quedaron por debajo del promedio son: {listaB}')
