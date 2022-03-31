def modifico_parametro(x):
    x = 10


a = 2
modifico_parametro(a)
print(a)

def modifico_parametro1(x):
    x[0] = "cero"

lista = [1, 20]
modifico_parametro1(lista)
print(lista)

def modifico_lista(x):
    y = x[:]
    y[0] = "cero"
    
lista = [1,20]
modifico_lista(lista)
print(lista)

