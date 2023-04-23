# Leia o primeiro termo e a razao de uma PA.
# NO final mostre os 10 primeiros termos dessa PA.

total = []
termos = []
pt = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão: "))
decimo = pt + (10 - 1) * razao # formula matematica pra achar o termo
for c in range(pt, decimo + razao, razao):
    termos = c
    total.append(termos)
print(total)