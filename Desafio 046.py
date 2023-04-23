# mostra na tela uma contagem regressiva para o estouro
# de fogos de artificio, indo de 10 até 0, com uma pausa de 1s.

import time
contador = 11
print('Contagem regresssiva para a virada de ano!🕐')
while contador > 0:
    contador = contador - 1
    time.sleep(1)
    print(f'{contador}..')
print('Feliz Ano novo!!')
