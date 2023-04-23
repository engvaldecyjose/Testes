# ler o ano de nascimento e informe de acordo com a idade:
# - se ainda vai se alistar ao serviço militar
# se é hora de se alistar
# se ja passou do tempo de alistamento
# mostrar o tempo que falta ou que passou do prazo

from datetime import date
ano = int(input("Digite o ano de nascimento: "))
anoatual = date.today().year  # para pegar o ano atual
idade = anoatual - ano

if idade < 18:
    alistar = 18 - idade
    futuro = anoatual + alistar
    print(f"Ano de nascimento:{ano}")
    print(f"Quem nasceu em {ano} tem {idade} anos em {anoatual}")
    print(f"Ainda faltam {alistar} anos para o alistamento")
    print(f"Seu alistamento será em {futuro}")

elif idade == 18:  # se atentar que o sinal de iogual é == e não = (atribuição)

    print(f"O ano de nascimento: {ano}")
    print(f'Quem nasceu em {ano} tem {idade} anos em {anoatual}')
    print(f'Você precisa se alistar imediatamente!')

elif idade > 18:
    teralistado = ano + 18  # ou ter feito idade - 18, seria mais pratico
    alistamento = anoatual - teralistado



    print(f"O ano de nascimento: {ano}")
    print(f'Quem nasceu em {ano} tem {idade} anos em {anoatual}')
    print(f'Você deveria ter se alistado há {alistamento} anos atrás')