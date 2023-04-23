# Calcule a soma entre todos os numeros impares que
# sao multiplos de tres e que se encontram no intervalo de 1 ate 500.

'''contador = 0
soma = 0
while contador < 501:
    contador = contador +1
    if contador % 2 == 1 and contador % 3 == 0:
       soma = soma + contador
print(soma)'''

# Sempre que souber um intervalo de repetição use o for
soma = 0
cont = 0 # Pra saber quantos valores foram somados
for c in range(1, 501, 2): # ele vai começar em 1 e pulando de 2 em dois, ou seja os impares
    if c % 3 == 0:
        soma = soma + c
        cont += 1
print(f"A soma de {cont} valores são {soma}")
