peso = float(input("Insira o peso em kg: "))
regiao = input("Insira a região (Sudeste, Sul, Norte, Nordeste, Centro-Oeste): ").lower()
premium = input("Você é assinante premium (sim/nao)?: ").lower()

if regiao == "sudeste":
    valor = 10 + (peso * 2)
elif regiao == "sul":
    valor = 15 + (peso * 3)
elif regiao == "norte" or regiao == "nordeste":
    valor = 25 + (peso * 5)
elif regiao == "centro-oeste":
    valor = 20 + (peso * 4)
else:
    valor = 0
    print("A região inserida não existe no Brasil.")

if valor > 0:
    if peso > 20:
        valor = valor + 30

    if premium == "sim":
        valor = valor * 0.80

    print(f"O valor final do frete: R$ {valor:.2f}")