import json

ARQUIVO = "estoque.json"

def carregar_estoque():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_estoque(estoque):
    with open(ARQUIVO, "w") as f:
        json.dump(estoque, f, indent=4)

def adicionar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    estoque = carregar_estoque()
    estoque.append({"nome": nome, "quantidade": quantidade, "preco": preco})
    salvar_estoque(estoque)
    print("Produto adicionado!")

def listar_produtos():
    estoque = carregar_estoque()
    total = 0
    print("\n=== Produtos no Estoque ===")
    for p in estoque:
        print(f"{p['nome']} - {p['quantidade']} unidades - R${p['preco']:.2f} cada")
        total += p['quantidade'] * p['preco']
    print(f"Valor total do estoque: R${total:.2f}")

def menu():
    while True:
        print("\n=== Controle de Estoque ===")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

menu()