# Ler o nome idade e sexo de 4 pessoas.
# No final do programa mostrar:
# - a media de idade do grupo,
# - qual e o nome do homem mais velho,
# - quantas mulheres tem menos de 20 anos.

# Criar listas vazias para armazenar dados das pessoas

somaidade = 0
homemvelho = 0
nomevelho = ''
cont = 0
mediaidade = 0

# Ler o nome das 4 pessoas
for i in range(0, 4):
    print(f'-----{i+1}ª Pessoa -----:')
    nome = str(input("Digite o nome da pessoa: "))
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo: [M/F] ")).upper()[0]  # tudo maiusculo e pega so a primeira letra
    somaidade += idade

    # Teste do homem mais velho
    if sexo == 'M':
        if idade > homemvelho:
            homemvelho = idade
            nomevelho = nome

    # Teste mulher menor que 20 anos
    if sexo == 'F':
        if idade < 20:
            cont += 1


# Media de idades, por meio da lista de idades
mediaidade = somaidade / 4
print(f"A media de idade é {mediaidade}")
# Soma de idade
print(f'A soma das idades do grupo é {somaidade}')
# Nome do homem mais velho
print(f'O nome do Homem mais velho é {nomevelho} e ele tem {homemvelho}')
# Quantas mulheres tem menos de 20 anos
print(f'O grupo tem {cont} mulheres com menos de 20 anos.')