"""• Queremos ingresar un número desde el teclado e imprimir si es múltiplo de 2, 3 o 5.
• Pista: Python tiene otra forma de la sentencia condicional: if-elif-else.
"""

num=int(input('Ingresa el numero: '))

for i in range(2,6):
    if num % i==0:
        print(f'El numero {num} es multiplo de {i}')