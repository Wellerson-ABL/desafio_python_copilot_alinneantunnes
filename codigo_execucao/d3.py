##3 - Operações Matemáticas Simples
##Vamos solicitar como entrada dois números e 
##depois vamos realizar uma operação simples entre eles.

# prof. com ajuda do copilot desktop, retornou esse modelo de codigo py
# que achei mais interessante.

print("Operações Matemáticas Simples")
numero1 = float(input("Digite o valor 1: "))
numero2 = float(input("Digite o valor 2: "))

## input 'Solicita dois números ao usuário' 
## float 'converte em  para permitir operações com decimais'

# Exibe as opções de operações
print("Escolha uma operação:")
print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")
opcao = int(input("Digite o número da operação:"))

# Realiza a operação escolhida e exibe o resultado
if opcao == 1:
    resultado = numero1 + numero2
    print("Resultado da soma:", resultado)
elif opcao == 2:
    resultado = numero1 - numero2
    print("Resultado da subtração:", resultado)
elif opcao == 3:
    resultado = numero1 * numero2
    print("Resultado da multiplicação:", resultado)
elif opcao == 4:
    resultado = numero1 / numero2
    print("Resultado da divisão:", resultado)
else:
    print("Operação inválida!")