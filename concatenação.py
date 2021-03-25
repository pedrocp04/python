# -*- coding: utf-8 -*-

"""strings
tipo de dados que se armazena coleçoes de caracteres
são declaradas entres as aspas
"""

#concatenação- strings aplicadas em duas variaveis

a = "Pedro"
b = "Eloara"

concatenar= a + " " + b
print(concatenar)

#verificando tamanho de string- conta espaço

tamanho = len(concatenar)
print(tamanho)

#navegação pelo indice- contagem começa pelo zero

print(a[0])
print(a[1])
print(a[2])

#imprimir um pedaço da string
# sintaxe--> var[x:y]

print(concatenar[1:])
print(concatenar[0:5])