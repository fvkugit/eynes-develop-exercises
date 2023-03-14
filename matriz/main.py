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

def findSequence(table):
    # Find 4 numbers horizontal sequence
    for row in table:
        for i in range(2):
            if row[i:i+4] == list(range(row[i], row[i]+4)):
                # If find sequence, print sequence coords.
                rowIndex = table.index(row)
                print(f"Secuencia horizontal desde [Fila {rowIndex}, Columna {i}] hasta [Fila {rowIndex}, Columna {i+3}].")
    # Find 4 numbers vertical sequence
    for j in range(5):
        for i in range(2):
            if [table[i+k][j] for k in range(4)] == list(range(table[i][j], table[i][j]+4)):
                # If find sequence, print sequence coords.
                print(f"Secuencia vertical desde [Fila {i}, Columna {j}] hasta [Fila {i+3}, Columna {j}].")

def printTable(table):
    for row in table:
        print(row)