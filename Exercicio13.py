import math
x_c = float(input("Insira a coordenada X do centro do círculo: "))
y_c = float(input("Insira a coordenada Y do centro do círculo: "))
r = float(input("Insira o raio: "))
x = float(input("Insira a coordenada X do ponto $P: "))
y = float(input("Insira a coordenada Y do ponto $P: "))

distancia = math.sqrt((x - x_c)**2 + (y - y_c)**2)

if distancia < r:
    print("Dentro do círculo")
elif distancia == r:
    print("Borda do círculo.")
else:
    print("Fora do círculo.")