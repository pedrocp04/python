# -*- coding: utf-8 -*-

#map--> pega uma função e aplica a todos elementos de uma lista

def dobro(x):
	return x*2

valor= [1, 2, 3, 4, 5]

#map(funçao,lista)
valor_dobrado = map(dobro, valor)

valor_dobrado = list(valor_dobrado)
print(valor_dobrado)

#ou

for v in valor_dobrado:
	print(v)