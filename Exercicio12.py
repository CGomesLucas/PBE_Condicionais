coluna_origem = str(input("Digite a letra do coluna onde o cavalo está cavalo: ")).upper()
linha_origem = int(input("Digite o número da linha onde o cavalo está cavalo: "))
coluna_destino = str(input("Digite a letra do coluna onde você quer que o cavalo vá: ")).upper()
linha_destino = int(input("Digite o número da linha onde você quer que o cavalo vá: "))

colunas = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

if not (1 <= linha_origem <= 8) or not (1 <= linha_destino <= 8):
    print("Insira um valor válido para a linha (1 a 8)")

if coluna_origem not in colunas or coluna_destino not in colunas:
    print("Insira um valor válida para a coluna (A a H")

distancia_euclidiana = (colunas.index(coluna_destino) - colunas.index(coluna_origem)) ** 2 + (linha_destino - linha_origem) ** 2

if distancia_euclidiana != 5:
    print("Posição inválida!")
else:
    print("Posição válida!")
