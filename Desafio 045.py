# crie um programa que faça o computador jogar jokempô com vc
# pedra papel e tesoura
from random import randint
import time

print('-'*25)
print('     JOKENPÔ AI')
print('-'*25)

print('É capaz de ganhar da AI? \nEscolha uma opção abaixo')
print('1) Pedra\n2) Papel\n3) Tesoura')
vc = int(input('\nQual vai ser o seu jogo?\n'))
ai = randint(1, 3)

print('Jo...')
time.sleep(0.5)
print('ken...')
time.sleep(0.5)
print('Pô!')
time.sleep(1)

if vc == 1 and ai == 3:
    print('Você escolheu Pedra e a AI Tesoura')
    print('Você Venceu!\nPedra ganha de tesoura!')

elif vc == 1 and ai == 2:
    print('Você escolheu Pedra e a AI Papel')
    print('Você Perdeu!\nPapel ganha de Pedra')

elif vc == 2 and ai == 1:
    print('Você escolheu Papel e a Ai Pedra')
    print('Voce venceu!\nPapel ganha de Pedra.')

elif vc == 3 and ai == 1:
    print('Você escolheu Tesoura e a AI Pedra')
    print('Você perdeu!\nPedra ganha de Tesoura')

elif vc == 3 and ai == 2:
    print('Você escolheu Tesoura e a Ai Papel')
    print('Você venceu!\nTesoura ganha de Papel')

elif vc == 2 and ai == 3:
    print('Você escolheu papel e a Ai escolheu Tesoura')
    print('Você Perdeu!\nPapel perde para Tesoura')

elif (vc == 1 and ai == 1) or (vc == 2 and ai == 2) or (vc == 3 and ai == 3):
    print('Empate! Tente de novo!')