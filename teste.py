qtd =0
soma =0
media =0
valor = float(input("digite um valor :"))

while (valor > 0.0):
        soma = soma + valor
        qtd = qtd + 1
        #entrega de valores
        valor = float(input("Digite um valor: "))
#caso digite um valor negatico o laço encerra
media = soma / qtd
print("\n Total da Soma: ", soma)
print("\n Quantidade de valores digitados: ", qtd)
print("\n Média dos valores: ", media)
