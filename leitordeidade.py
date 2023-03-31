##leitor de situação eleitoral pela idade

idade = int(input("Digite sua idade para saber sua situação eleitoral: "))

if idade < 15:
    print("Não eleitor")
elif idade <= 17:
    print("Eleitor facultativo")
elif idade <= 64:
    print("eleitor obrigatório")
else:
    print("eleitor facultativo")
