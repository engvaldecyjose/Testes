# Ler seis numeros inteiros, e mostre a soma dos
# valores pares apenas, o impar desconsidera

soma = 0
for c in range(1, 7):
    num = int(input("Digite um valor:"))
    if num % 2 == 0:
        soma += num
print(f"A soma dos numeros pares digitados é {soma}")