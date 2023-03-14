"""
    Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
    números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
    final.
"""
import random 
import doctest


def numbersTable(length):
    """
        Generate a table of random numbers (length x length)

        Args:
            length (int): Length of rows and columns on the table

        Returns:
            table (list): List of rows 
        
        Example:
            # Test generating a 5x5 table with random numbers (seed 1)
            >>> random.seed(1) # Ensure consistent results
            >>> numbersTable(5)
            [[2, 9, 1, 4, 1], [7, 7, 7, 6, 3], [1, 7, 0, 6, 6], [9, 0, 7, 4, 3], [9, 1, 5, 0, 0]]

            # Test generating a 7x7 table with random numbers (seed 3)
            >>> random.seed(3) # Ensure consistent results
            >>> numbersTable(7)
            [[3, 9, 8, 2, 5, 9, 7], [9, 1, 9, 0, 7, 4, 8], [3, 3, 7, 8, 8, 7, 6], [2, 3, 2, 8, 6, 0, 1], [2, 9, 0, 4, 0, 4, 7], [9, 6, 6, 6, 9, 7, 2], [5, 1, 0, 2, 7, 3, 4]]
            
            # Test generating a 5x5 table with random numbers (seed 8)
            >>> random.seed(8) # Ensure consistent results
            >>> numbersTable(5)
            [[3, 5, 6, 2, 3], [0, 1, 2, 3, 8], [3, 6, 0, 7, 7], [7, 6, 7, 9, 3], [6, 1, 7, 3, 0]]
    """
    # Create 5x5 table of random numbers between 0 and 9 
    table = [[random.randint(0, 9) for j in range(length)] for i in range(length)]
    return table

def findSequence(table):
    """
        Find a sequence of 4 consecutive numbers (horizontally or vertically) on a table
        In case of find a sequence, print coords of numbers sequence.

        Args:
            table (list): List of rows
        
        Returns:
            -

        Example:
            # Test find sequence on 5x5 table with seed 1 (no-sequence)
            >>> random.seed(1) # Ensure consistent results
            >>> table = numbersTable(5)
            >>> findSequence(table)

            # Test find sequence on 5x5 table with seed 8 (horizontal sequence on row 1)
            >>> random.seed(8) # Ensure consistent results
            >>> table = numbersTable(5)
            >>> findSequence(table)
            Secuencia horizontal desde [Fila 1, Columna 0] hasta [Fila 1, Columna 3].
    """
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

if __name__ == "__main__":
    doctest.testmod()