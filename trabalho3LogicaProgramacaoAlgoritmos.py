#listas do enunciado
tipoMadeira = {
    "PIN": 150.40,
    "PER": 170.20,
    "MOG": 190.90,
    "IPE": 210.10,
    "IMB": 220.70
}

tipoTransporte = {
    1: 1000,
    2: 2000,
    3: 2500
}

#função menu

def menu():
    print("Entre com o tipo de madeira desejado")
    print("PIN - Tora de Pinho")
    print("PER - Tora de Peroba")
    print("MOG - Tora de Mogno")
    print("IPE - Tora de Ipê")
    print("IMB - Tora de Imbuia")

#função para escolher o tipo de madeira 

def escolha_tipo():
    while True:
        menu()
        
        tipo = input().upper().strip()
    
        if tipo in tipoMadeira:
            return tipoMadeira[tipo]
        else:
            print("Escolha inválida, entre com o modelo novamente")
        print()


#função para calcular quantidade e desconto de toras

def qtd_toras():
    while True:
        try:
            total_toras = int(input("Entre com a quantidade de toras (m³): "))
        except ValueError:
            print("Erro: digite apenas números inteiros!")
            continue

        if (total_toras < 100):
            desconto = 0

        elif (total_toras < 500):
            desconto = 0.04
            print("desconto de 4%")
        
        elif (total_toras < 1000):
            desconto = 0.09
            print("desconto de 9%")
        
        elif (total_toras < 2000):
            desconto = 0.16
            print("desconto de 16%")
        
        elif (total_toras > 2000):
            print("não é aceito pedidos com essa quantidade de toras")
            continue
        else:       
            return None, None
    
        return total_toras, desconto

#função para escolher o modelo de transporte a ser usado

def transporte():
    while True:
        print("Escolha o tipo de Transporte:")
        print("1 - Transporte Rodoviário  - R$ 1000.00")
        print("2 - Transporte Ferroviário - R$ 2000.00")
        print("3 - Transporte Hidroviário - R$ 2500.00")
    
        modal = int(input())
   
    
        if modal in tipoTransporte:
            valor = tipoTransporte[modal]
            return valor
        else:
            print("Opção inválida")
            return 0
    
#sistema principal

print("\nBem vindo à Madereira do Lenhador Allef da Silva Bastos\n")
while True:
    precoMadeira = escolha_tipo()
    total_toras, desconto= qtd_toras()
    valor_transporte = transporte()
    

    total = ((precoMadeira * total_toras)*(1-desconto)) + valor_transporte
    print(f"Total: R$ {total:.2f}")
    break
