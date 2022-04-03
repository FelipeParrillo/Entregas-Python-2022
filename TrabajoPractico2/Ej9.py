"""9. La idea es tratar de programar una de las partes principales del juego “Buscaminas”. La idea
es que dado una estructura que dice que celdas tienen minas y que celdas no las tienen, como
la siguiente:
[
'-*-*-',
'--*--',
'----*',
'*----',
]
Generar otra que indique en las celdas vacías la cantidad de bombas que la rodean, para el ejemplo
anterior, sería:
[
'1*3*1',
'12*32',
'1212*',
'*1011',
]
"""

           
estructura = ['-*-*-',
              '--*--',
              '----*',
              '*----']

def crearMatriz(matriz):
    """Agarra la la lista 'estructura' y convierte cada string dentro en otra lista para convertirla en una matriz y facilitar su recorrido"""
    for i in range(len(estructura)):
        matriz.append(list(estructura[i]))


def recorrerMatriz(matriz):
    """Recorre la matriz revisando todos los posibles existentes puntos al rededor de la posicion a evaluar y suma al contador cuando hay una bomba"""
    for x in  range(len(matriz)):
        for y in range(len(matriz[x])):
            #verifico que la pos a evaluar es una casilla libre de bomba
            if (matriz[x][y] == '-'): 
                cont=0
                # hago un try al rededor de la pos a evaluar por si existe un index out of range
                try:
                    if matriz[x-1][y-1]=='*':
                        cont+=1
                    if matriz[x][y-1]=='*':
                        cont+=1
                    if matriz[x+1][y-1]=='*':
                        cont+=1
                    if matriz[x+1][y]=='*':
                        cont+=1
                    if matriz[x+1][y+1]=='*':
                        cont+=1
                    if matriz[x][y+1]=='*':
                        cont+=1
                    if matriz[x-1][y+1]=='*':
                        cont+=1
                    if matriz[x-1][y]=='*':
                        cont+=1
                    
                except: print(f'this position  matriz[{x}][{y}] does not exist (index out of range)')
                matriz[x][y]=cont
    
    for n in range(len(matriz)):
        matriz[n]=matriz[n]
        print(matriz[n])


                
matriz=[]
crearMatriz(matriz)
recorrerMatriz(matriz)
