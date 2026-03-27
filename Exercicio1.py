import math

while True:
    h0 = float(input("Informe a altura inicial:"))
    if h0 < 0:
        break
    else:
        resultado = math.sqrt(h0 / 4.9)
        print("O resultado é", resultado)




