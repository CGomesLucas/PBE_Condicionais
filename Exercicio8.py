valor_saque = int(input("Insira o valor que você deseja sacar:"))
valor_restante = valor_saque
notas_disponiveis = [100, 50, 20, 10, 5, 2]
resultado = {}

for nota in notas_disponiveis:
    quantidade_notas = valor_restante // nota
    resultado[nota] = int(quantidade_notas)
    valor_restante -= quantidade_notas * nota

if valor_restante > 0:
    print("Valor impossível de sacar com as notas disponíveis")
    print(f"Resto R$ {valor_restante:.2f}")
else:
    for nota, qtd in resultado.items():
        if qtd > 0:
            print(f"Notas de R$ {nota}: {qtd}")