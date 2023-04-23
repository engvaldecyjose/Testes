# leia um numero e diga se ele e inteiro, e diga
# se ele é ou nãoi numero primo (divide por 1 e ele mesmo)
"""
num = input("Digite um número: ")
tipo = type(num)
print(tipo)
if num % 1 == 0 and num % num == 0:
    print("É um número primo")
else:
    print("Não é um numero primo")"""

num = int(input("Digite um numero: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='') # O end é pra nao pular de linha, e o que estiver dentro do '' vai aparecer entres os prints
        tot += 1
    else:
        print('\033[m', end='')
    print(f"{c}", end=" ")
print(f"\n\033[mO numero {num} foi divisivel {tot} vezes")

if tot == 2: # pra ser primo so pode duas vezes
    print("Ele é primo")
else:
    print("Ele não é primo")