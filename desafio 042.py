# desafio 35 dos triangulos,
# fazer verificação se é um triangulo e dizer qual triangulo é!
# a soma de dois lados do triangulço tem que ser sempre maior que o outro lado dele
print('-'*25)
print('Que tipo de triângulo é:')
print('-'*25)

m1 = int(input('Digite o valor 1: '))
m2 = int(input('Digite o valor 2: '))
m3 = int(input('Digite o valor 3: '))

# Verificação (pelo menos duas verificações)

if (m1 + m2) > m3 and (m2 + m3) > m1:
    print('Esse triângulo existe.')
    if m1 == m2 and m1 == m3:
        print('Ele é um triângulo Equilátero')
    elif m1 != m2 and m2 != m3 and m3 != m1:
        print('Ele é um triângulo Escaleno')
    elif m1 == m2 != m3 or m1 == m3 != m2 or m3 == m2 != m1:
        print('Ele é um triângulo Isósceles')
