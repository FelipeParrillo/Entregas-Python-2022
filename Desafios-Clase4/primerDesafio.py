from collections import Counter
import csv
import os 

ruta = os.path.dirname(os.path.realpath("."))
ruta_archivo = os.path.join('C:\\Users\\felay\\OneDrive\\Documentos\\Lenguajes-VsCode\\Python-Actividades\\Entregas-Python-2022\\Desafios-Clase4\\netflix_titles.csv')
ruta_archivo
archivo = open(ruta_archivo, "r", encoding='utf8') 
    
csvreader = csv.reader(archivo, delimiter=',')

#leyendo el encabezado para que no moleste en el filtrado de datos 
encabezado = next(csvreader)

# Functions #

def Filtrar():
    list_pelis_2021=[]
    list_pais_productor = []
    for linea in csvreader:
        # Agregando a una lista las peliculas agregadas a netflix en 2021
        if '2021' in linea[6] and linea[1] == 'Movie':
            list_pelis_2021.append(linea[2]) 
    
        # Agregando a una lista el pais de producción de una temporada/pelicula
        if linea[5] != '':
            list_pais_productor.append(linea[5])
    
    return list_pelis_2021,list_pais_productor


def imprimir(list_2021,c):
    #print tabla con top 5 productores
    mas_comunes = c.most_common(5)
    print('TOP Producciones   | Cant Producciones' )
    print('-'*19 + '+' + '-'*19)
    for i in range(5):
        print(f'{mas_comunes[i][0]:<18} | {mas_comunes[i][1]:>4}')
        print('-'*19 + '+' + '-'*19)

    print('\n \n \n ')
    
    #print pelis agregadas en 2021
    print('*'*63)
    print('*                 Pelis Agregadas en 2021                     *')
    print('*'*63)
    for peli in list_2021:
        print(f'* {peli:<60}*') 
    print('*'*63)

# __Main__ #
list_pelis,list_prod = Filtrar()
c = Counter(list_prod)
imprimir(list_pelis,c)
archivo.close()