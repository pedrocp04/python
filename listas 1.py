# -*- coding: utf-8 -*-

"""listas
conjunto de dados

--numericas
--strings
--> sempre declaradas entre []
"""

minha_lista = ["abacaxi", "melancia", "abacate"]

#print(minha_lista)

minha_lista2 = [1,2,3,4,5]

#print(minha_lista2)

minha_lista3 = ['abacaxi', 2, 9.89, True]

#print(minha_lista3)

#print(minha_lista[0])

"""for item in minha_lista:
	print (item)
"""
tamanho = len(minha_lista)

#print(tamanho)

#add elementos

minha_lista.append("limão")

print(minha_lista)

#verificar se um elemento existe na lista

if 3 in minha_lista2:
	print("3 esta na lista")

#remover elementos

del minha_lista[2:]
print(minha_lista)

#apagar toda lista
del minha_lista[:]
print(minha_lista)

minha_lista4 = []

minha_lista4.append(57)

print(minha_lista4)