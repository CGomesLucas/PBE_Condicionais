hora_inicial = int(input("Hora inicial: "))
minuto_inicial = int(input("Minuto inicial: "))
hora_final = int(input("Hora final: "))
minuto_final = int(input("Minuto final: "))

minutos_inicial = hora_inicial * 60 + minuto_inicial
minutos_final = hora_final * 60 + minuto_final

duracao_total = minutos_final - minutos_inicial

if duracao_total <= 0:
    duracao_total += 24 * 60

qtd_horas = duracao_total // 60
qtd_minutos = duracao_total % 60

print(f"O jogo durou {qtd_horas} horas e {qtd_minutos} minutos")