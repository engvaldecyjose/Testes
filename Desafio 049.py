# Refaça o exercicio 009, mostrando a tabuada de um numero
# que o usuario escolher, so que agora utilizando o laço for

num = int(input("Digite a tabuada desejada: "))
for c in range(1, 11):
    tab = num * c
    print(f"{num} x {c} = {tab}")