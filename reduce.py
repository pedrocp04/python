# -*- coding: utf-8 -*-

"""reduce
--> recebe uma lista e retorna so um valor da lista, como uma soma
"""

from functools import reduce

def soma(x,y):
	return x+y
lista = [1, 3, 5, 10, 20]

#var = reduce(funçao, lista)
soma = reduce(soma, lista)
print(soma)