# calcular valor a ser pago por um produto
# considerando o preço normal, condição de pagamento:

# a vista dinheiro ou pix: 10% de desconto
# a vista no cartao 5% desconto
# em ate 2x no cartao = preço normal
# 3x ou mais, 20% de juros

print('-'*25)
print('Forma de pagamento')
print('-'*25)

valor = float(input("Digite o valor do produto: \nR$"))
print('_'*25)
print('Forma de pagamento: ')
print('1) À vista dinheiro ou pix.\n2) à vista no cartão.')
print('3) Até 2x no cartão sem juros.\n4) 3x ou mais no cartão com juros.')
print('_'*25)

op = int(input('Digite a opção desejada: '))

if op == 1:
    desconto = valor - (valor * 0.10)
    print(f'O valor a ser pago é: R${desconto}')
elif op == 2:
    desconto = valor - (valor * 0.05)
    print(f'O valor a ser pago é: R${desconto}')
elif op == 3:
    print(f'O valor a ser pago é 2x R${valor/2}')
elif op == 4:
    juros = valor * 1.2
    xx = float(input("Quantas parcelas? "))
    print(f'O valor a ser pago é {xx}x de R${juros/xx}')
    print(f'O valor total da compra será de R${juros} por causa dos juros')