"""
    Hacer una función que genere una lista de diccionarios que contengan id y edad, donde
    edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10
    elementos. retornar la lista.
    Hacer otra función que reciba lo generado en la primer función y ordenarlo de mayor a
    menor. Printear el id de la persona más joven y más vieja. Devolver la lista ordenada.
"""
import random

def generateList(long):
    list = []
    for i in range(10):
        user = {'id': i, 'edad': random.randint(1, 100)}
        list.append(user)
    return list

def sortList(list):
    min, max = [0, 0]
    sortedList = sorted(list, key=lambda x: x['edad'], reverse=True)
    min = sortedList[-1]['id']
    max = sortedList[0]['id']
    print(f"Persona mas joven ID: {min}\nPersona mas vieja ID: {max}")
    return sortedList

