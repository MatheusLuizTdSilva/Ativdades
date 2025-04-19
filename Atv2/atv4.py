usuarios = {
    "admin": {"senha": "1234", "saldo": 0, "transacoes": []}
}

def login():
    user = input("Usuário: ")
    senha = input("Senha: ")
    if user in usuarios and usuarios[user]["senha"] == senha:
        print("Login bem-sucedido!")
        menu_banco(user)
    else:
        print("Usuário ou senha inválidos.")

def deposito(usuario):
    valor = float(input("Valor para depositar: "))
    usuarios[usuario]["saldo"] += valor
    usuarios[usuario]["transacoes"].append(f"Depósito: +R${valor:.2f}")
    print("Depósito realizado.")

def saque(usuario):
    valor = float(input("Valor para sacar: "))
    if valor <= usuarios[usuario]["saldo"]:
        usuarios[usuario]["saldo"] -= valor
        usuarios[usuario]["transacoes"].append(f"Saque: -R${valor:.2f}")
        print("Saque realizado.")
    else:
        print("Saldo insuficiente.")

def extrato(usuario):
    print("\n=== Extrato ===")
    for t in usuarios[usuario]["transacoes"]:
        print(t)
    print(f"Saldo atual: R${usuarios[usuario]['saldo']:.2f}")

def menu_banco(usuario):
    while True:
        print("\n=== Banco ===")
        print("1. Depósito")
        print("2. Saque")
        print("3. Ver Extrato")
        print("4. Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            deposito(usuario)
        elif opcao == "2":
            saque(usuario)
        elif opcao == "3":
            extrato(usuario)
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

login()