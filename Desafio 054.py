# leia o ano de ansc de 7 pessoas e no final
# mostrar quantas pessoas nao atingiram a maior idade
# maior idade de 21 anos


cont = 0
for i in range(1, 8):
    idade = int(input("Digite a idade: "))
    if idade < 21:
        cont += 1
print(f'Dentre as 7 pessoas, {cont} são menores de idade')
