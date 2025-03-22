##3 - Operações Matemáticas Simples
##Vamos solicitar como entrada dois números e 
##depois vamos realizar uma operação simples entre eles.

num1 = int(input(""))
num2 = int(input(""))

operacao = input("Digite a operaçao que deseja realizar (+,-,*,/): ")
if operacao == '+':
print(num1 + num2)

elif operacao == '-':
print(abs(num1 - num2))

else:
print("Operação inválida")