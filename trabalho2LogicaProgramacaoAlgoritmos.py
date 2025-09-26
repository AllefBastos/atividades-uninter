# Mensagem de boas-vindas com nome e sobrenome
def menu():
    print("-" * 10 +"Bem vindo ao sistema do Allef da Silva Bastos"+ "-" * 10)
    print("-" * 28 +"Cardápio"+ "-" * 29)
    print("-" * 65)
    print("---|" "  Tamanho  |   Pizza Salgada (PS)   |   Pizza Doce(PD)   |---")
    print("---|" "     P     |       R$ 30.00         |     R$ 34.00       |---" )
    print("---|" "     M     |       R$ 45.00         |     R$ 48.00       |---" )
    print("---|" "     G     |       R$ 60.00         |     R$ 66.00       |---" )

# Tabela de preços do enunciado
precos = {
    "PS": {"P": 30.00, "M": 45.00, "G": 60.00},
    "PD": {"P": 34.00, "M": 48.00, "G": 66.00}
}

total = 0.0
menu()

# condicional para selecionar tamanho e sabor
while True:
    
    # Escolhendo o sabor
    sabor = input("Entre com o sabor desejado (PS/PD): ").upper()
    if sabor not in ["PS", "PD"]:
        print("Sabor inválido. Tente novamente\n")
        continue

    # Escolhendo o tamanho
    tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper()
    if tamanho not in ["P", "M", "G"]:
        print("Tamanho inválido. Tente novamente\n")
        continue

    # Mostrar pedido
    preco = precos[sabor][tamanho]
    tipo = "Pizza Salgada" if sabor == "PS" else "Pizza Doce"
    print(f"Você pediu uma {tipo} no tamanho {tamanho}: R$ {preco:.2f}\n")

    total += preco

    # Perguntar se deseja mais algo
    mais = input("Deseja mais alguma coisa? (S/N): ").upper()
    if mais == "N":
        break

print(f"\nO valor total a ser pago: R$ {total:.2f}")

