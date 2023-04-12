##leitor de condição eleitoral pela idade

1 idade = int(input("Digite a sua idade: "))
2 if idade < 16:
3 categoria = 'não-eleitor'
4 elif idade >= 18 and idade <= 65:
5
categoria = 'eleitor obrigatório'
6 else:
7 categoria = 'eleitor facultativo'
8 print("Sua classe eleitoral é:", categoria)
