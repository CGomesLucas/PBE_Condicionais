valor = float(input("Insira o valor que você deseja sacar:"))

notas_disponiveis = [100, 50, 20, 10, 5, 2]

valor_devolvido = []

if valor not in notas_disponiveis:
    print("Esse valor é impossível de ser sacado!")

for x in notas_disponiveis:
    if valor < x:
        valor_devolvido += x
        
        
      

