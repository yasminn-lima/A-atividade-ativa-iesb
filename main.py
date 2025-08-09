print('hello Word')
# Coffee Shops Tia Rosa - Sistema de Gerenciamento

#Listas para guardar os dados 
clientes = []
produtos = []
pedidos = []

#Função principal (menu)
def menu():
    while True:
        print("\n====== COFFEE SHOPS TIA ROSA ======")
        print("1 - Cadastrar cliente")
        print("2 - Cadastrar produto")
        print("3 - Fazer pedido")
        print("4 - Mostrar pedidos")
        print("5 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_cliente()
        elif escolha == '2':
            cadastrar_produto()
        elif escolha == '3':
            fazer_pedido()
        elif escolha == '4':
            mostrar_pedidos()
        elif escolha == '5':
            print("Saindo do sistema... Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente!")

def cadastrar_cliente():
    print("\n--- Cadastro de Cliente ---")
    nome = input("Nome do cliente: ")
    telefone = input("Telefone: ")
    cliente = {'nome': nome, 'telefone': telefone}
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def cadastrar_produto():
    print("\n--- Cadastro de Produto ---")
    nome = input("Nome do produto: ")
    preco = float(input("Preço (ex: 7.50):R$ "))
    produto = {'nome': nome, 'preco': preco}
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def fazer_pedido():
    print("\n--- Fazer Pedido ---")
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("\nClientes cadastrados:")
    for i, cliente in enumerate(clientes):
        print(f"{i+1}. {cliente['nome']}")

    cliente_id = int(input("Escolha o número do cliente: ")) - 1

    print("\nProdutos disponíveis:")
    for i, produto in enumerate(produtos):
        print(f"{i+1}. {produto['nome']} - R${produto['preco']:.2f}")

    produto_id = int(input("Escolha o número do produto: ")) - 1

    pedido = {
        'cliente': clientes[cliente_id]['nome'],
        'produto': produtos[produto_id]['nome'],
        'preco': produtos[produto_id]['preco']
    }

    pedidos.append(pedido)
    print("Pedido registrado com sucesso!")

def mostrar_pedidos():
    print("\n--- Pedidos Realizados ---")
    if not pedidos:
        print("Nenhum pedido foi feito ainda.")
        return
    for p in pedidos:
        print(f"{p['cliente']} pediu {p['produto']} - R${p['preco']:.2f}")

menu()
