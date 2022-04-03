"""6. Dada una frase donde las palabras pueden estar repetidas e indistintamente en mayúsculas y
minúsculas, imprimir una lista con todas las palabras sin repetir y en letra minúscula.
"""

frase = """
Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple.
"""

frase = frase.lower().replace(',', '').replace('.', '').split()

filtrado = []
for n in range(len(frase)):      # agarra la frase y mientras las palabras no esten en la nueva lista filtrado, las va agregando, asi queda una lista sin repetir palabras
    if frase[n] not in filtrado:
        filtrado.append(frase[n])


print(filtrado)
