# ler peso e altura de uma pessoa
# calcule o IMC e mostre o status

# abaixo de 18,5: abaixo do peso
# entre 18,5 e 25: peso ideal
# 25 ate 30: sobrepeso
# 30 ate 40: obesidade
# acima de 40: obesidade morbida

print('-'*25)
print('Calculo de IMC')
print('-'*25)

peso = float(input("Digite seu peso em kg: "))
altura = float(input('Digite sua altura em m: '))
print(f'\nVocê tem {peso}kg e {altura}m')

imc = peso/(altura ** 2)
print(f'Seu IMC é = {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!')
elif 25 <= imc < 30:
    print('Você está em Sobrepeso!')
elif 30 <= imc < 40:
    print('Você está em Obesidade!')
elif imc >= 40:
    print('Você esta em Obesidade mórbida!')