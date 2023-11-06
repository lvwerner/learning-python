arquivo = open('arquivo.txt', 'w')

arquivo.write('Esse é o meu arquivo.\n')
arquivo.write('Aula Prática de Python\n')
arquivo.close()

#leitura do arquivo

leitura = open('arquivo.txt', 'r')
print(leitura.read())
leitura.close()