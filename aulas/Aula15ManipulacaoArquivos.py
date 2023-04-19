#Métodos para manipulação de arquivos
#open("caminho do arquivo",parâmetro) - cria ou abre um arquivo txt
#read() - lê o conteúdo de arquivo txt
#readlines() - lê o conteúdo e retorna uma lista
#write() - escreve uma linha
#writelines() - escreve várias linhas de uma só vez utilizando Lista

#Parâmetros método open
#w - cria/abre o arquivo e sobreescreve (apaga o que tinha e escreve) (write)
#a - cria/abre o arquivo e escreve no final (append)
#r - lê o conteúdo do arquivo (read) - default (não precisa colocar)

#1. Lendo arquivos

#1.1 Lê todas as linhas do arquivo
arquivo = open("C:\Temp\ArquivoPython.txt", "r")
print(arquivo.read())

#1.2 Lê todas as linhas do arquivo utilizando uma Lista
arquivo = open("C:\Temp\ArquivoPython.txt", "r")
palavras = list() #ou palavras=[]
palavras = arquivo.readlines()
for p in palavras:
    print(p)

#2. Criando e escrevendo nos arquivos

#2.1 Cria e/ou escreve no arquivo linha por linha
arquivo = open("C:\Temp\ArquivoPython.txt", "a")
arquivo.write("Aula\n")
arquivo.write("Top\n")
arquivo.write("Python")

#2.2 Cria/escreve no arquivo várias linhas de uma vez utilizando uma Lista
arquivo = open("C:\Temp\ArquivoPython.txt", "a")
palavras = list()
palavras.append("Aula\n")
palavras.append("Top\n")
palavras.append("Python")
arquivo.writelines(palavras)

#2.3 Sobrescreve o conteúdo do arquivo (parâmetro w)
arquivo = open("C:\Temp\ArquivoPython.txt", "w")
arquivo.write("Alooou")