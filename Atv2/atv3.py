ASSENTOS = ["Livre"] * 10  # 10 assentos

def mostrar_assentos():
    print("\n=== Mapa de Assentos ===")
    for i, a in enumerate(ASSENTOS):
        status = "🟩 Livre" if a == "Livre" else "🟥 Reservado"
        print(f"Assento {i + 1}: {status}")

def reservar_assento():
    mostrar_assentos()
    num = int(input("Número do assento para reservar: ")) - 1
    if 0 <= num < len(ASSENTOS):
        if ASSENTOS[num] == "Livre":
            ASSENTOS[num] = "Reservado"
            print("Reserva feita com sucesso!")
        else:
            print("Esse assento já está reservado.")
    else:
        print("Número inválido.")

def cancelar_reserva():
    mostrar_assentos()
    num = int(input("Número do assento para cancelar: ")) - 1
    if 0 <= num < len(ASSENTOS):
        if ASSENTOS[num] == "Reservado":
            ASSENTOS[num] = "Livre"
            print("Reserva cancelada.")
        else:
            print("Esse assento já está livre.")
    else:
        print("Número inválido.")

def menu():
    while True:
        print("\n=== Sistema de Reservas ===")
        print("1. Mostrar Assentos")
        print("2. Reservar Assento")
        print("3. Cancelar Reserva")
        print("4. Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            mostrar_assentos()
        elif opcao == "2":
            reservar_assento()
        elif opcao == "3":
            cancelar_reserva()
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

menu()