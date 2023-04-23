
# leia um ano e diga se é bissexto
# qualquewr ano que seja divisivel por 4 é um ano bissexto
# exceto multiplos de 100 que nao sao divisiveis por 400

#biblioteca Datetime, vai mostrar data e hora

ano = int(input("Digite um ano para saber se ele é Bissexto: \n"))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Sim, o ano ", ano," é Bissexto")
else:
    print(ano, "não é Bissexto")