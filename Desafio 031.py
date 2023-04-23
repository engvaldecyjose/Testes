# pergunta a distancia em km, calcule o preço da passagem,
# 0,50 por km ate 200km e 0,45 para mais lkongas

km = float(input("Qual a distancia da viagem em km? \n"))
if km >= 200:
    valor = (km * 0.45)
    print("O valor da passagem é: R$", valor)
else:
    valor = (km * 0.5)
    print("O valor da passagem é: R$", valor)