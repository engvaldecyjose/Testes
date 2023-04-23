import time
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
ai = randint(0, 2)


print('-'*15)
print('  Jokempo AI')
print('-'*15)

print('Consegue ganhar da ai?\nEscolha uma opção abaixo: ')
print('0) Pedra\n1) Papel\n2)Tesoura')
vc = int(input('Qual é o seu jogo? '))

print('-='*8)
print(f'A AI jogou {itens[ai]}')
print(f'Você jogou {itens[vc]}')
print('-='*8)

print('JO...')
time.sleep(0.5)
print('KEN...')
time.sleep(0.5)
print('PO!')
time.sleep(1)

if ai == 0:
    if vc == 0:
        print('\nEmpate!')
    elif vc == 1:
        print('\nVocê Perdeu!')
    elif vc == 2:
        print('\nVocê Ganhou!')

if ai == 1:
    if vc == 0:
        print('\nVocê Perdeu!')
    elif vc == 1:
        print('\nEmpatou!')
    elif vc == 2:
        print('\nVocê Venceu!')

if ai == 2:
    if vc == 0:
        print('\nVocê Venceu!')
    if vc == 1:
        print('\nVocê Perdeu!')
    if vc == 2:
        print('\nEmpatou!')