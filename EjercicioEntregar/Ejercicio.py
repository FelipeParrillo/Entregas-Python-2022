def main():
    import csv
    import openpyxl

    ruta_archivo = 'Python-Actividades\Entregas-Python-2022\EjercicioEntregar\BBB_nuevo.csv'
    archivoBBB = open(ruta_archivo, "r", encoding='utf8')
    csvreader = csv.reader(archivoBBB, delimiter=',')
    encabezado = next(csvreader)

    #_Functions_#
    def Filtrar():
        '''Retorna una lista con los datos de los usuarios que vieron una clase y reprodujeron una grabación'''
        lista_verificada = []
        lista_grabacion = []
        lista_visualizada = []
        lista_usuarios = []
        # Agrego por IP a la lista correspondiente segun la "Actividad" hecha
        for linea in csvreader:
            if linea[2] == 'Actividad BigBlueButtonBN visualizada':
                lista_visualizada.append(linea[4])

            if linea[2] == 'Grabación vista':
                lista_grabacion.append(linea[4])
                lista_usuarios.append(linea[1])

        # Corroboro que la IP haya visto por lo menos una grabacion  y haya estado en una clase
        for n in range(len(lista_grabacion)):
            if (lista_grabacion[n] in lista_visualizada):
                lista_verificada.append([lista_usuarios[n], ''])

        return lista_verificada

    def exportar_archivo(lista):
        '''Genera un archivo y exporta la lista pasada como parametro'''
        wb = openpyxl.Workbook()
        hoja = wb.active
        # Pasaje del encabezado
        hoja.append(['Nombres'])
        # Pasaje de datos
        for prod in lista:
            hoja.append(prod)
        wb.save("BBB_Actualizado.csv")

    #_Main_#
    lista = Filtrar()
    exportar_archivo(lista)


if __name__ == "__main__":
    main()
