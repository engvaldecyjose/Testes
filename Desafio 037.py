# ler um numero qualquer e pedir pro usuario escolher qual vai ser
# a base de conversão:
# 1 para binario
# 2 para octal
# 3 para hexadecimal

num = int(input("Digite o numero para conversão: \n"))
print("----" * 14)
print("Escolha abaixo o número da base de conversão desejada: ")
print("----" * 14)
print("\n1) Binário")
print("2) Octal")
print("3) Hexadecimal")

x1 = int(input("\nDigite o número da opção desejada: \n"))

'''converter para binario usa-se a função bin() mas ele vai sair
com um "ob" na frente, pra tirar usa-se a funçao format pra formatar a saida
b = binario
o = octal
x =hexadecimal'''


if x1 == 1:
    x2 = format(num, "b")
    print(f"O número {num:.2f} em Binario é {x2}")
if x1 == 2:
    x2 = format(num, "o")
    print(f"O número {num:.2f} em Octal é {x2}")
if x1 == 3:
    x2 = format(num, "x")
    print(f"O número {num:.2f} em Hexadecimal é {x2}")