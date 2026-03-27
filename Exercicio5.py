velocidade = int(input("Insira a velocidade do carro:"))
limite = int(input("Insira o limite da via:"))

if limite > 100:
    tolerancia = limite + (limite * 0.07)
    if velocidade < tolerancia:
        print("isento")
    elif velocidade > (tolerancia + (tolerancia * 0.20)):
        print("Multa média")
    elif (tolerancia + (tolerancia * 0.20)) < velocidade < (tolerancia + (tolerancia * 0.50)):
        print("Multa grave")
    elif velocidade > (tolerancia + (tolerancia * 0.50)):
        print("Gravíssima + Suspensão")
else:
    tolerancia = limite + 7
    if velocidade < tolerancia:
        print("Isento")
    elif velocidade > (tolerancia + (tolerancia * 0.20)):
        print("Multa média")
    elif (tolerancia + (tolerancia * 0.20)) < velocidade < (tolerancia + (tolerancia * 0.50)):
        print("Multa grave")
    elif velocidade > (tolerancia + (tolerancia * 0.50)):
        print("Gravíssima + Suspensão")


    

