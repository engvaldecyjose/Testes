# pergunta e escreva o salario
# e calcule o aumento
# superiores a 1250 o aumento e 10%
# inferiores ou iguais o aumento é 15%

sal = float(input("Digite o seu salário: \nR$"))

if sal > 1250:
    sal2 = sal * 1.10
    print(f"Você teve aumento de 10% e seu salário foi para R${sal2:,.2f}")
else:
    sal2 = sal * 1.15
    print(f"Você teve aumento de 15% e seu salário foi para R${sal2:.2f}")