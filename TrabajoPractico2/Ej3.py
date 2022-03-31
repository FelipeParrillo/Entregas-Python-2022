

text = """Dado un texto solicite por teclado una letra e imprima las palabras que comienzan con dicha
letra. En caso que no se haya ingresado una letra, indique el error. Ver: módulo string"""


def leeCaracter():
    """funcion que valida el ingreso de un solo caracter y que sea una letra"""
    while True:
        print('Ingresa una letra: ')
        letra = input().lower()
        if letra.isalpha() and 1 == len(letra):
            return letra
        else:
            print('No se ingreso UNA sola letra')


letra = leeCaracter()
palabras = []

# Manjeo de String para que no tenga puntos y comas + pasarlo a minusculas y separarlo en una lista
text = text.replace(".", '')
text = text.replace(",", '')
text = text.lower().split()


for i in range(len(text)):  # recorrer lista hasta encontrar las palabras q empiezan con la letra ingresada, no toma repetidas
    if text[i][0] == letra:
        if text[i] not in palabras:
            palabras.append(text[i])
print(palabras)
