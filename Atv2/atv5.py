import json

ARQUIVO = "contatos.json"

def carregar_contatos():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_contatos(contatos):
    with open(ARQUIVO, "w") as f:
        json.dump(contatos, f, indent=4)

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    contatos = carregar_contatos()
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    salvar_contatos(contatos)
    print("Contato adicionado!")

def buscar_contato():
    nome = input("Buscar por nome: ").lower()
    contatos = carregar_contatos()
    encontrados = [c for c in contatos if nome in c["nome"].lower()]
    if encontrados:
        for c in encontrados:
            print(f"{c['nome']} - {c['telefone']} - {c['email']}")
    else:
        print("Nenhum contato encontrado.")

def menu():
    while True:
        print("\n=== Gerenciador de Contatos ===")
        print("1. Adicionar Contato")
        print("2. Buscar Contato")
        print("3. Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            buscar_contato()
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

menu()