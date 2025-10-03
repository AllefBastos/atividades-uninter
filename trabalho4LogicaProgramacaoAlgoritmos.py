# variaveis do enunciado

lista_contatos = []
id_global = 5541357

# função parara cadastrar contatos

def cadastrar_contato(id): 
    print("-" * 12 +" MENU CADASTRAR CONTATO " + "-" * 12)
    print(f"Id do Contato: {id}")
    nome = input("Por favor entre com o nome do Contato: ")
    atividade = input("Por favor entre com a Atividade do contato: ")
    telefone = input("Por favor entre com o telefone do Contato: ")

    
    contato = {
        "id": id,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }

    lista_contatos.append(contato.copy())   

# função para consultar contatos

def consultar_contatos():
    print("-" * 40)
    print("-" * 7 +" MENU CONSULTAR CONTATOS " + "-" * 8)
    print("Escolha a opção desejada:")
    print("1 - Consultar Todos os Contatos")
    print("2 - Consultar Contato por id")
    print("3 - Consultar Contato(s) por Atividade")
    print("4 - Retornar")

    op = int(input())

    if not lista_contatos:
        print("\n Nenhum contato cadastrado ainda.\n")
        return
    
    if (op == 1):
        for contato in lista_contatos:
            print("-" * 15)
            print(f"id: {contato['id']} \nnome: {contato['nome']} \natividade: {contato['atividade']} \ntelefone: {contato['telefone']}")
    
    elif (op == 2):
        opId = int(input("Digite o id do contato: "))
        encontrado = False

        for contato in lista_contatos:
            if contato["id"] == opId:
                print(f"id: {contato['id']} \nnome: {contato['nome']} \natividade: {contato['atividade']} \ntelefone: {contato['telefone']}")
                encontrado = True
                
        if not encontrado:
            print("Contato não encontrado.")

    elif (op == 3):
        opAt = (input("Digite a atividade do contato: "))
        encontrado = False

        for contato in lista_contatos:
            if contato["atividade"] == opAt:
                print(f"id: {contato['id']} \nnome: {contato['nome']} \natividade: {contato['atividade']} \ntelefone: {contato['telefone']}")
                encontrado = True
                

        if not encontrado:
            print("Contato não encontrado.")
        

    elif (op == 4):
        return
    
    else:
        print("Opção inválida. Tente novamente!")

# função para remover contatos

def remover_contato():
    while True:
       id_remover = int(input("Digite o id do contato a ser removido: "))

       encontrado = False

       for contato in lista_contatos:

           if contato["id"] == id_remover:

               lista_contatos.remove(contato)

               print("Funcionário removido com sucesso.")

               encontrado = True

               break

       if not encontrado:
           print("Id inválido")
       else:
           break

#programa principal

print("Bem vindo a lista de contatos do Allef da Silva Bastos") 
while True:
        print("-" * 40)
        print("-" * 12 +" MENU PRINCIPAL " + "-" * 12)
        print("Escolha a opção desejada:")
        print("1 - Cadastrar Contato")
        print("2 - Consultar Contato(s)")
        print("3 - Remover Contato")
        print("4 - Sair")

        op = int(input())

        if (op == 1):
            cadastrar_contato(id_global)
            id_global += 1

        elif (op == 2):
            consultar_contatos()
        elif (op ==3):
            remover_contato()
        elif (op == 4):
            break
        else:
            continue
