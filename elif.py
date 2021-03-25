# -*- coding: utf-8 -*-

"""elif
caso haja necessidade de mais condições entre o if e o else

if condição:
	execute_esta_linha
elif condição:
	execute
else:
	execute
"""

x = 1
y = 2

if x == y:
	print("numeros iguais")
elif x < y:
	print("x menor que y")
elif y > x:
	print("y maior que x")
else:
	print("numeros diferentes")

# executa primeira consição que tiver