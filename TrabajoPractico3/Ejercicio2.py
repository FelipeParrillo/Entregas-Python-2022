# Function #

def load_data():
    '''Retorna una lista con los datos del data_set'''
    # Aprovecho la funcion del Ejercicio1.py y tan solo le mando como parametro el nombre del archivo
    import Ejercicio1
    datos = Ejercicio1.read_file('BBB_nuevo.csv')
    return datos


def most_common_week_day(datos):
    '''Retorna una tupla (dia_de_semana_mayor_registros , cant_registros)'''
    import datetime
    from collections import Counter

    formato = "%d/%m/%Y %H:%M"
    dias_semana = ['lunes', 'martes', 'miercoles',
                   'jueves', 'viernes', 'sabado', 'domingo']

    # Paso los datos leidos a string y los junto todos en una unica cadena ya que es la estructura que soporta Counter
    lista = "".join(list(map(lambda x:  str(
        datetime.datetime.strptime(x[0], formato).weekday()), datos)))

    mas_comun = Counter(lista).most_common(1)
    tupla = (dias_semana[int(mas_comun[0][0])], mas_comun[0][1])
    return tupla


def day_amount(datos):
    """Retorna una varaible TimeDelta, con la cant de tiempo entre el primer y ultimo registro"""
    import datetime
    formato = "%d/%m/%Y %H:%M"
    # Abusamos de que el data_set esta ordenado por fecha, y no hay que iterarlo para saber el maximo y minimo
    frst_registter = datetime.datetime.strptime(datos[0][0], formato)
    last_registter = datetime.datetime.strptime(datos[len(datos)-1][0], formato)
    time_dif = frst_registter - last_registter

    return time_dif

# Main

def main():
    datos = load_data()
    print(most_common_week_day(datos))
    print(day_amount(datos))
    
if __name__ == '__main__':
    main()

