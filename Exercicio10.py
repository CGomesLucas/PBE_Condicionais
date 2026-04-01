import re

senha = input("Crie sua senha: ")
regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s]).{8,}$"

if len(senha) < 8:
    print("Inválida: Menos de 8 caracteres.")

elif re.match(regex, senha):
    print("Forte: Letras maiúsculas, minúsculas, números e caracteres especiais.")

elif senha.isdigit() or senha.islower():
    print("Fraca: Só letras minúsculas ou só números")

else:
    print("Média: Mistura de letras e números.")