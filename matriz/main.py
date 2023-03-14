"""
    Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
    números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
    final.
"""

import random 

def numbersTable(length):
    # Create 5x5 table of random numbers between 0 and 9 
    table = [[random.randint(0, 9) for j in range(length)] for i in range(length)]
    return table