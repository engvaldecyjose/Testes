# leia dois numeros inteiros e os compare mostrando a mensagem:
# o primeiro valor e maior
# o segundo valor e maior
# nao existe valor maior os dois sao iguais

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if num1 > num2:
    print(f"O primeiro valor {num1} é maior")
if num2 > num1:
    print(f"O segundo valor {num2} é maior")
if num1 == num2:
    print("Não existe valor maior, os dois são iguais")