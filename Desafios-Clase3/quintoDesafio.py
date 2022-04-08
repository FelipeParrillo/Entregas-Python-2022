"""Usando expresiones lambda escribir una función que permita codificar una
frase según el siguiente algoritmo:

encripto("a") --> "b"
encripto("ABC") --> "BCD"
encripto("Rock2021") --> "Spdl3132"
"""




def encripto(text):
    '''Recibe una string y la encripta en cifrado César'''
    palabra=[]
    text.split()                             # me da error y no entiendo porque
    for n in text:                           # aux=[]
        palabra.append(chr(ord(n)+1))        # aux. append(chr (lambda (x: ord(x)+1,n) ) )
    aux=''
    return aux.join(palabra)

E=encripto('abcd')
print(E)

