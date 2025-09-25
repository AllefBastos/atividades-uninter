# Mensagem de boas-vindas com nome e sobrenome
print("Bem vindo ao sistema do Allef da Silva Bastos")

# Entrada de dados conforme o enunciado
valorBase = float(input("Informe o valor Base do plano: "))
idade = int(input("Informe a idade do cliente: "))

# Variaveis para a estrutura condicional
tabela = 0
valorMensal = 0


# Estrutura condicional para definir a porcentagem conforme a idade usando if, elif e else
if (idade >= 0 and idade < 19):
    tabela = 100
    valorMensal = valorBase * (tabela / 100)
    print(f"O valor mensal do plano é de: R$ {valorMensal:.2f}")

elif (idade >= 19 and idade < 29):
    tabela = 150
    valorMensal = valorBase * (tabela / 100)
    print(f"O valor mensal do plano é de: R$ {valorMensal:.2f}")

elif (idade >= 29 and idade < 39):
    tabela = 225
    valorMensal = valorBase * (tabela / 100)
    print(f"O valor mensal do plano é de: R$ {valorMensal:.2f}")

elif (idade >= 39 and idade < 49):
    tabela = 240
    valorMensal = valorBase * (tabela / 100)
    print(f"O valor mensal do plano é de: R$ {valorMensal:.2f}")

elif (idade >= 49 and idade < 59):
    tabela = 350
    valorMensal = valorBase * (tabela / 100)
    print(f"O valor mensal do plano é de: R$ {valorMensal:.2f}")

else:
    tabela = 600
    valorMensal = valorBase * (tabela / 100)
    print(f"O valor mensal do plano é de: R$ {valorMensal:.2f}")



