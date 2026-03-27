dia = int(input("Insira o dia que você nasceu:"))
mes = int(input("Insira o mes que você nasceu:"))
ano = int(input("Insira o ano que você nasceu:"))

if mes == "Janeiro" or"Março" or "Maio" or "Julho" or "Agosto" or "Outubro" or "Dezembro":
    if dia < 0 or dia > 31:
        print("Dia inválido")

if mes == "Abril" or "Junho" or "Setembro" or "Novembro":
    if dia < 0 or dia > 30:
        print("Dia inválido")

if mes == "Fevereiro":
    if dia < 0 or dia > 29:
        print("Dia inválido")
        
if  not 1900 < ano < 2026:
    print("Ou você é Imortal ou é um viajante do futuro")


