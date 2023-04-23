# Escreva um proggrama que leia a velocidade de um carro

# se ele ultrapassar 80km/h mostre uma mensagem dizendo que foi multado
# a multa vai custar 7,00 por cada km acima do limite

velo = float(input("Digite a velocidade registrada do automovel: \n"))
if velo > 80:
    print("Você ultrapassou a velocidade!")
    multa = velo - 80
    valor = multa * 7
    print("O valor da multa é de: R$", valor,)
else:
    print("Parabens, você esta dentro do limite!")