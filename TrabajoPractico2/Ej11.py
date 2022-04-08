def duped(archN1, archN2):
    '''Retorna una lista con los nombres duplicados de ambas strings '''
    nombres1 = archN1.replace(',', '').replace("'", "").split()
    nombres2 = archN2.replace(',', '').replace("'", "").split()

    dup = [x for x in nombres1 if x in nombres2]
    return dup

def Imprimir(archN1, archP1, archP2):
    ''' Imprime en Columnas los datos de cada String pasado'''
    nombres = archN1.replace(',','').replace("'","").lower().split()
    p1 = archP1.replace(',','').split()
    p2 = archP2.replace(',','').split()
    

    

    print('    | Nombre     | Nota1      | Nota2      | Total   ')
    for n in range(len(nombres)):
        print(f'{n:3} | {nombres[n]:10} | {p1[n]:10} | {p2[n]:10} | {(int(p1[n]) + int(p2[n])):<3}')






# Abro los archivos y los paso a strings
with open("Python-Actividades\\Entregas-Python-2022\\TrabajoPractico2\\nombres_1.txt", encoding="utf8") as archivo_nombres1:
    archN1 = archivo_nombres1.read()
with open("Python-Actividades\\Entregas-Python-2022\\TrabajoPractico2\\nombres_2.txt", encoding="utf8") as archivo_nombres2:
    archN2 = archivo_nombres2.read()
with open("Python-Actividades\\Entregas-Python-2022\\TrabajoPractico2\\eval1.txt", encoding='utf8') as archivo_prueba1:
    archP1 = archivo_prueba1.read()
with open("Python-Actividades\\Entregas-Python-2022\\TrabajoPractico2\\eval2.txt", encoding='utf8') as archivo_prueba2:
    archP2 = archivo_prueba2.read()

dup = duped(archN1, archN2)
print(f'Los nombres que se encunetran en ambos son: {dup}')

Imprimir(archN1, archP1, archP2)