# -*- coding: utf-8 -*-

"""manipulação de arquivos

funçao open
--> var= open(nome, modo)

modo:
r ---> somente leitura
w ---> escrita (caso o arquivo já exista, ele será
apagado e um novo arquivo vazio será criado)
a ---> leitura e escrita(adiciona o novo conteudo
no fim do arquivo)
r+ ---> leitura e escrita
w+ ---> escrita (apaga o conteudo do arquivo anterior)
a+ ---> leitura e escrita (abre o arq pra att)

funçoes:
read() ---> le o arq todo
readline()---> le uma linha
readlines()---> le arq e o armazena em uma lista
"""
arq = open("arq.txt")

"""linhas = arq.readlines()

for linha in linhas:
	print(linhas)
"""
"""texto = arq.read()

print(texto)
"""

w = open("arq.txt","a")

w.write("esse é o meu arq\n")

w.close()
