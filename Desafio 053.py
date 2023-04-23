# leia uma frase qualquer e diga se ela e
# um palindromo desconsiderando os espaços.
# Palindromo pode ler de tras pra frente e ser a mesma coisa


frase = input("Digite sua frase para verificação de palindromo: ")
fraseb = frase.replace(" ", '') # Para tirar os espaços
print(fraseb)
fraseinvert = fraseb[::-1] # para deixar a frase invertida
print(fraseinvert)
if fraseb == fraseinvert:
    print('=-'*15)
    print('Essa frase é um palindromo')
    print('=-' * 15)
else:
    print('=-' * 15)
    print('\nEssa frase não é um palindromo')
    print('=-' * 15)