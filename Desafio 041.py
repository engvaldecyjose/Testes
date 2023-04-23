# Mostrar a categoria do atleta de acordo com a idade dele

# ate 9 anos = mirim
# ate 14 = infantil
# ate 19 = junior
# ate 20 = senior
# acima = master

from datetime import date
print('-'*25)
print('Classificação de atletas')
print('-'*25)

ano = int(input('\nDigite o ano do nascimento: '))
atual = date.today().year
idade = atual - ano
print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Atleta Mirim.')

elif 9 < idade <= 14:
    print('Atleta Infantil.')

elif 14 < idade <= 19:
    print('Atleta Junior.')

elif 19 < idade <= 20:
    print('Atleta Sênior.')

elif idade > 20:
    print('Atleta Master.')