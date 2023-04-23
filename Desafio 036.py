# Programa para aprovar um emprestimo bancario para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salario do comprador
# e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não
# pode exceder 30% do salario ou então o emprestimo sera negado.

valor = float(input("Qual é o valor da casa? \n"))
salario = float(input("Qual é o seu salario? \n"))
tempo = int(input("Em quantos anos pretende pagar? \n"))

cond = salario * 0.3
parcela = valor / tempo
mensal = parcela / 12

if mensal <= cond:
    print("Para pegar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}".format(valor, tempo, mensal))
    print("Emprestimo Concedido!")
else:
    print("Emprestimo Negado!")