imposto_1 = 0
imposto_2 = 0
imposto_3 = 0
valor_liquido = 0

salario_bruto = float(input("Digite o seu salario bruto:"))

if 2000 < salario_bruto < 4000:

    imposto_1 = (salario_bruto -  (4000 - 2000)) * 0.10 
    valor_liquido = salario_bruto - imposto_1 

elif 4000 < salario_bruto < 8000:
     
     imposto_2 = ((salario_bruto - (8000 - 4000)) * 0.20) + imposto_1
     valor_liquido = salario_bruto - imposto_1

elif salario_bruto > 8000:
    iomposto_3 = (((salario_bruto - 8000) * 0.30) + imposto_1 + imposto_2) 
    valor_liquido = salario_bruto - imposto_3

else: 
    print("Isento de imposto EBAAAAAAAAAAAAA")

imposto_total = imposto_1 + imposto_2 + imposto_3 

print(salario_bruto)
print(imposto_total)
print(valor_liquido)

     
