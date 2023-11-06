def adicionar(x, y):
   return x + y

def subtrair(x, y):
   return x - y

def multiplicar(x, y):
   return x * y

def dividir(x, y):
   return x / y

print("Selecione a operação.")
print("1.Adicionar")
print("2.Subtrair")
print("3.Multiplicar")
print("4.Dividir")

escolha = input("Escolha uma operação(1/2/3/4):")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if escolha == '1':
   print(num1,"+",num2,"=", adicionar(num1,num2))

elif escolha == '2':
   print(num1,"-",num2,"=", subtrair(num1,num2))

elif escolha == '3':
   print(num1,"*",num2,"=", multiplicar(num1,num2))

elif escolha == '4':
   print(num1,"/",num2,"=", dividir(num1,num2))
else:
   print("Entrada inválida")