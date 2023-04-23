# Leia duas notas de aluno e calcule sua media
# mostre uma mensagem final, de acordo com a media atingida
# media 5.0 = aprovado
# media entre 5,0 e 6,9 = recuperação
# média superior a 7,0 = aprovado

print("-"*20)
print("Situação na matéria")
print('-'*20)

nota1 = float(input("\nDigite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2)/2

if media >= 7.0:
    print("\nAprovado!")

elif 5.0 <= media <= 6.9:
    print("\nRecuperação")

elif media < 5.0:
    print("\nReprovado")

print("-"*20)