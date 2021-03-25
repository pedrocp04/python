# -*- coding: utf-8 -*-

#pode aplicar metodos a strings
# string= string.metodo()

#alterar caixa .lower()

"""a =  "Pedro"
b = "Pigatto"

concatenar= a + " " + b + " "

print(concatenar)
print(concatenar.lower())

#maiusculo .upper()

print(concatenar.upper())
print(concatenar)

#strip- remove espaço e caractere especial

print(concatenar.strip())

#split- converte a string em uma lista"""

minha_string = "o rato roeu a roupa do rei de Roma"

"""minha_lista = minha_string.split()

print(minha_lista)

minha_lista2 = minha_string.split("r")
print(minha_lista2)"""

#buscando substring-- pedaço de uma string

busca = minha_string.find("rei")

print(busca)

print(minha_string[busca:])

"""busca2 = minha_string.find("rainha")

print(busca2)"""

#substituir partes de uma string

minha_string= minha_string.replace("o rei", "a rainha")
print(minha_string)