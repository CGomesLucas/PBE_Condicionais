import math

a = int(input("Insira o valor de a:"))
b = int(input("Insira o valor de b:"))
c = int(input("Insira o valor de c:"))
x1 = 0
x2 = 0

if a == 0:
    print("Não é equação do segundo grau!")

else:

    delta = (b**2) - (4 * a * c)

    if delta < 0:
        print("A equação não possui raízes reais")
    else:
        x1 = (-b + math.sqrt(delta)) / 2 * a
        x2 = (b + math.sqrt(delta)) / 2 * a

    print(delta)
    print(x1, x2)


