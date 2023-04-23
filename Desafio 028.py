# Escreva um programa que fgaço o computador "pensAR"
# em um numero inteiro entre 0 e 5 e peça para o usuario tentar
# descobrir qual foi o numero escolhido pelo computador.

# O progreama devera escrever na tela se o usuario venceu ou perdeu

# > Para gerar numero aleatorio usa a função: Randint(x,y) gerar entre x a y

import random
ai = random.randint(0, 5)
print("A Inteligencia Artificial escolheu um numero entre 0 e 5, você é capaz de adivinhar?")
num = int(input("Digite um numero entre 0 e 5: \n"))
if num == ai:
    print("Parabéns você acertou!")
else:
    print("Que pena, você errou!")
    op = str(input("Deseja tentar novamente? s/n: \n"))
    if op == "s":
        num = int(input("Digite o numero entre 0 e 5, segunda tentativa!: \n"))
        if num == ai:
            print("Parabéns você acertou!")
        else:
            print("Que pena, você errou!")
            op = str(input("Deseja tentar novamente? s/n: \n"))
            if op == "s":
                num = int(input("Digite o numero entre 0 e 5, ultima tentativa!: \n"))
                if num == ai:
                    print("Parabéns você acertou!")
                else:
                    print("Que pena, você errou!")
