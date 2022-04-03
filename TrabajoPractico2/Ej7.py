"""Escriba un programa que solicite que se ingrese una palabra o frase y permita identificar si la
misma es un Heterograma (tenga en cuenta que el contenido del enlace es una traducción del
inglés por lo cual las palabras que nombra no son heterogramas en español). Un Heterograma
es una palabra o frase que no tiene ninguna letra repetida entre sus caracteres"""


texto = input('Ingrese una frase/palabra: ').lower().replace(',','').replace('.','')

lista=texto.split()

print(lista)


for i in range(len(lista)):
    dup=[]
    heterograma=True
    for j in range(len(lista[i])):
        
        if lista[i][j] not in dup:
            dup.append(lista[i][j])
        else:
            heterograma=False
    if heterograma:
        print(f'La palabra: {lista[i]} es un heterograma')
    else:
        print(f'La palabra: {lista[i]} no ')
