from datetime import datetime

opcoes = [
        "1 - Criar Contato",
        "2 - Listar Contatos",
        "3 - Atualizar Contato",
        "4 - Deletar Contato",
        "5 - Buscar Contato",
        "6 - Encerrar"
]
def menu():
    while True:
        print("\n- MENU PRINCIPAL -\n")

        for opcao in opcoes:
            print(opcao)

        escolha = input("\nEscolha uma opção: ")

        match escolha:
            case '1':
                print("\n** criar_contato **\n")
            case '2':
                print("\n** listar_contatos  **\n")
            case '3':
                print("\n** Atualizar Contato **\n")  
            case '4':
                print("\n** Deletar Contato **\n")  
            case '5':
                print("\n** Buscar Contato **\n")  
            case '6':
                print("\n** Programa Encerrado **\n")
                break
            case _:
                print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    print(datetime.now().strftime("%d/%m/%Y, %H:%M"))
    menu()