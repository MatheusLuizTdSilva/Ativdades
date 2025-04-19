import json
from datetime import datetime

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)

def adicionar_tarefa():
    descricao = input("Descrição da tarefa: ")
    prazo = input("Prazo (AAAA-MM-DD): ")
    tarefas = carregar_tarefas()
    tarefas.append({"descricao": descricao, "prazo": prazo, "concluida": False})
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    tarefas = sorted(carregar_tarefas(), key=lambda x: x["prazo"])
    for i, t in enumerate(tarefas):
        status = "V" if t["concluida"] else "X"
        print(f"{i + 1}. {t['descricao']} | Prazo: {t['prazo']} | Concluída: {status}")

def concluir_tarefa():
    listar_tarefas()
    num = int(input("Número da tarefa a concluir: ")) - 1
    tarefas = carregar_tarefas()
    if 0 <= num < len(tarefas):
        tarefas[num]["concluida"] = True
        salvar_tarefas(tarefas)
        print("Tarefa marcada como concluída!")
    else:
        print("Número inválido.")

def menu():
    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

menu()