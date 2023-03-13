"""
    Hacer una función que genere una lista de diccionarios que contengan id y edad, donde
    edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10
    elementos. retornar la lista.
    Hacer otra función que reciba lo generado en la primer función y ordenarlo de mayor a
    menor. Printear el id de la persona más joven y más vieja. Devolver la lista ordenada.
"""
import random
import doctest

def generateList(length):
    """
        Generate a list of dictionaries with 'id' and (randomly generated) 'edad' keys.

        Args:
            length (int): Length of generated list

        Returns:
            generatedList: List of dictionaries, each dict have 'id' and 'edad' keys.

        Example:
            # Test generating a list with length of 10
            >>> random.seed(1) # Ensure consistent results
            >>> generateList(10)
            [{'id': 0, 'edad': 18}, {'id': 1, 'edad': 73}, {'id': 2, 'edad': 98}, {'id': 3, 'edad': 9}, {'id': 4, 'edad': 33}, {'id': 5, 'edad': 16}, {'id': 6, 'edad': 64}, {'id': 7, 'edad': 98}, {'id': 8, 'edad': 58}, {'id': 9, 'edad': 61}]
            
            # Test generating a list with length of 3
            >>> random.seed(1) # Ensure consistent results
            >>> generateList(3)
            [{'id': 0, 'edad': 18}, {'id': 1, 'edad': 73}, {'id': 2, 'edad': 98}]
    """
    generatedList = []
    for i in range(length):
        user = {'id': i, 'edad': random.randint(1, 100)}
        generatedList.append(user)
    return generatedList

def sortList(unsortedList):
    """
        Sort desc a list with 'id' and 'edad' keys using 'edad' as sort key.

        Args:
            unsortedList (list): List of dictionaries with 'id' and 'edad' keys.

        Returns:
            list: A list of dicts sorted in desc order by 'edad' key.

        Example:
            # Test sorting list [10 length]
            >>> random.seed(1) # Ensure consistent results
            >>> list1 = generateList(10)
            >>> sortList(list1) # Sort generated list
            Persona mas joven ID: 3
            Persona mas vieja ID: 2
            [{'id': 2, 'edad': 98}, {'id': 7, 'edad': 98}, {'id': 1, 'edad': 73}, {'id': 6, 'edad': 64}, {'id': 9, 'edad': 61}, {'id': 8, 'edad': 58}, {'id': 4, 'edad': 33}, {'id': 0, 'edad': 18}, {'id': 5, 'edad': 16}, {'id': 3, 'edad': 9}]
            
            # Test sorting list [3 length]
            >>> random.seed(1) # Ensure consistent results
            >>> list2 = generateList(3)
            >>> sortList(list2) # Sort generated list
            Persona mas joven ID: 0
            Persona mas vieja ID: 2
            [{'id': 2, 'edad': 98}, {'id': 1, 'edad': 73}, {'id': 0, 'edad': 18}]
    """
    min, max = [0, 0]
    sortedList = sorted(unsortedList, key=lambda x: x['edad'], reverse=True)
    min = sortedList[-1]['id']
    max = sortedList[0]['id']
    print(f"Persona mas joven ID: {min}\nPersona mas vieja ID: {max}")
    return sortedList


# Functions test, should print the initial list, the younger and older user in list and the sorted list.
if __name__ == "__main__":
    doctest.testmod()

