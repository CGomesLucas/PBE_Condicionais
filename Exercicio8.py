valor = float(input("Insira o valor que você deseja sacar:"))

notas_disponiveis = [100, 50, 20, 10, 5, 2]

valor_devolvido = []

if valor == 1 or valor == 3:
    print("Esse valor é impossível de ser sacado")
else:

    for x in notas_disponiveis:
        valores = valor / x
        valor_devolvido.append(valores)
        valor -= valores * x

        for y in range (len(notas_disponiveis)):
            print(f"{notas_disponiveis[y]}: {valor_devolvido[y]}")

        print(f"O resto é: {valor}")




