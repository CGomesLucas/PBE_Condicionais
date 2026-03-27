lado1 = float(input("Insira o primeiro lado do triângulo"))
lado2 = float(input("Insira o segundo lado do triângulo"))
lado3 = float(input("Insira o segundo lado do triângulo"))

if lado1 + lado2 < lado3 or lado2 + lado3 < lado1 or lado1 + lado3 < lado1:
    print("O triângulo não é válido")
else:
    escaleno = lado1 != lado2 != lado3
    equilatero = lado1 != lado2 != lado3
    isosceles = lado1 == lado2 or lado1 == lado3 or lado3 == lado1

    resultado = {"Equilatero": equilatero, "Escaleno": escaleno, "Isosceles": isosceles}
    print(resultado)

if lado1**2 + lado2**2 == lado3**2 or lado2**2 + lado3**2 == lado2**2 or lado3**2 + lado1**2 == lado2**2:
    print("O triângulo é equilátero")