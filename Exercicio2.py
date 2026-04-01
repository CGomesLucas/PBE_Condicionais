lado1 = float(input("Insira o primeiro lado do triângulo:"))
lado2 = float(input("Insira o segundo lado do triângulo:"))
lado3 = float(input("Insira o segundo lado do triângulo:"))

if lado1 + lado2 <= lado3 or lado2 + lado3 <= lado1 or lado1 + lado3 <= lado2:
    print("O triângulo não é válido!")
elif lado1 != lado2 != lado3:
    print("Triângulo Escaleno")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Triângulo Equilatero")
else:
    print("Triângulo Isósceles")

if lado1**2 + lado2**2 == lado3**2 or lado2**2 + lado3**2 == lado1**2 or lado1**2 + lado3**2 == lado2:
    print("O triângulo é retângulo")

