# ler o peso de 5 pessoas e no final
# mostrar qual foi o maior e o menor peso lido.

menor = 0
maior = 0
menorb = 0
for i in range(1, 6):
    idade = int(input("Digite o peso: "))
    if idade > maior:
        maior = idade
        menor = idade
    else:
        if menorb < menor:
            menorb = idade
print(f'O maior peso é {maior} e o menor é {menorb}')