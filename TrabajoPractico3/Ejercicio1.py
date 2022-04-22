'''1.1 Ejercicios
        1. Encontrar qué tipo de shows tiene un país determinado.
        • Realizar una función que informe todos los países que existen.
        • Realizar una función que dado un país informe si es parte de la línea del show pasado como
        argumento. Nota: utilice las funciones vistas de lambda(utilizando la función definida), map
        para informar los tipos de shows (valores únicos) en que participa un país.
Analizar:
• ¿En qué número de columna está el país?
• Como en algunos casos hay varios países en un show debemos separarlos y quedarnos con
valores únicos.
2. Informe la lista de países del archivo en orden alfabéticamente creciente.
3. Informe los shows de un año determinado, realice una función que reciba un año y la línea
como argumentos.
'''

# Funciones #
def read_file(file_name):
    '''Abre el archivo csv pasa los datos a una variable y lo cierrra'''
    import csv
    import os
    abspath = os.path.abspath(__file__)
    path, filename = os.path.split(abspath)
    os.chdir(path)
    archivo = open(file_name, 'r', encoding='utf8')
    lector = csv.reader(archivo, delimiter=',')
    datos = next(lector), list(lector)
    archivo.close()
    return datos[1]

def filtrar(lista):
    '''Recibe una lista, la limpia, saca vacios y saca espacios al principio/final'''
    lista = list(map(lambda x: x.split(','), lista))
    aux = []
    for listado in lista:        # esta doble iteracion fue la unica que se me re complico para pasarla a map con lambda y listarla de esa forma
        for l in listado:
            aux.append(l.strip())
    return list(filter(bool, set(aux)))

def find_country(datos):
    '''Retorna una lista con todos los paises que estan en el archivo'''
    return filtrar(list(map(lambda x: x[5], datos)))

def find_show_type(pais,datos):
    '''Retorna una lista con los tipos de shows que tiene un pais, en caso de que el pais no este en la lista retorna falso'''
    paises = find_country()

    if pais in paises:                
        generos_del_pais = list(filter(bool,set(map(lambda linea: linea[10] if pais in linea[5] else False, datos)))) # Quito los False de relleno porque el split no los soporta 
        return filtrar(generos_del_pais)
    else:
        return False

    
def search_by_country_show(pais, show, datos):
    '''Informa si el pais pasado contiene el show pasado o no, en caso de que el pais pasado no este en la lista de paises del data_set devuelve False'''
    paises  = find_country()
    if pais in paises:         
        lista = list(( map(lambda x : True if (show == x[2] and pais in list(x[5].split(', '))) else False ,datos)))
        if True in lista:
            return 'Contiene'
        else:
            return 'No contiene'
    else:
        return False

def alpha_order():
    '''Ordena alfabeticamete la lista de paises'''
    paises = find_country()
    paises.sort()
    return paises
         
def search_by_year(año,datos):
    '''Devuelve una lista con las pelis estrenadas en ese año'''
    lista = list(filter(bool, set(map(lambda x: x[2] if x[7] == año else False , datos))))
    return lista
    
# Main #
def main():
    datos = read_file('netflix_titles.csv')  # DATOS es una variable que uso practicamente en todas las funciones, ya que estoy consultando el data_set,
    print(find_country(datos))               # me pregunto si tiene que ser pasada como parametro o usar un var global, o como implementar su uso. 
    print(find_show_type('Argentina',datos))
    print(search_by_country_show('India', 'Kota Factory', datos))
    print(alpha_order())
    print(search_by_year('1990',datos))
    
if __name__ == "__main__":
    main()

