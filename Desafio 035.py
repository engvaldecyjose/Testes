# Leia o comprimento de tres retas e dizer se pode oui nao fromar um triagulo

# o que deve ter para formar um triangulo?
# um de seus lados deve ser maior que o valor absoluto
# (módulo) da diferença dos outros dois lados e menor que
# a soma dos outros dois lados.

x = int(input("Digite o valor de um lado do triangulo: \n"))
y = int(input("Digite o outro lado: \n"))
z = int(input("Digite o outro lado: \n"))

if (x + y) > z and (x + z) > y and (z + y) > x:
    print("Sim, essas dimensões podem formar um triângulo")
else:
    print("Não pode formar um triangulo")