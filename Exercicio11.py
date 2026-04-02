x1 = int(input("Insira o canto superior esquerdo X: "))
y1 = int(input("Insira o canto superior esquerdo Y: "))
x2 = int(input("Insira o canto inferior direito X: "))
y2 = int(input("Insira o canto inferior direito Y: "))

print("\nRetângulo 2:")
x3 = int(input("Insira o canto superior esquerdo X: "))
y3 = int(input("Insira o canto superior esquerdo Y: "))
x4 = int(input("Insira o canto inferior direito X: "))
y4 = int(input("Insira o canto inferior direito Y: "))

if x1 >= x4 or x3 >= x2 or y2 >= y3 or y4 >= y1:
    print("Os retângulos não se sobrepõem.")
else:
    print("Os retângulos se sobrepõem")