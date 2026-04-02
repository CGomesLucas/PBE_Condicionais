numero = int(input("Digite um número inteiro de exatamente 5 dígitos: "))

if numero < 10000 or numero > 99999:
    print("O número deve ter exatamente 5 dígitos.")
else:

    verificacao1 = numero // 10000
    verificacao2 = (numero // 1000) % 10
    verificacao3 = (numero // 100) % 10
    verificacao4 = (numero // 10) % 10
    verificacao5 = numero % 10

    if verificacao1 == verificacao5 and verificacao2 == verificacao4:
        print(f"O número {numero} é um palíndromo")
    else:
        print(f"O número {numero} não é um palíndromo.")
