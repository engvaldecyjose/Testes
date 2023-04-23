# Leias tres numeros e mostre qual e o maior e qual e o menor.

x = int(input("Digite o 1º número: \n"))
y = int(input("Digite o 2º número: \n"))
z = int(input("Digite o 3º número: \n"))
maior = 0
menor = 0

# Achar o maior
if x > y and x > z:
    maior = x

if y > x and y > z:
    maior = y

if z > x and z > y:
    maior = z

# Achar o menor
if x < y and x < z:
    menor = x
if y < x and y < z:
    menor = y
if z < x and z < y:
    menor = z

print("O maior entre os três valores é: ", maior,)
print("O menor entre os três valores é: ", menor,)