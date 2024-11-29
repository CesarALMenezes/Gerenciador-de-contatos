from datetime import datetime
from controladores import criar_contato, listar_contatos, atualizar_contato, deletar_contato
from os import system

opcoes_menu = [
    "1 - Listar Contatos",
    "2 - Criar Contato",
    "3 - Atualizar Contato",
    "4 - Deletar Contato",
    "5 - Encerrar",
]

def iniciar_menu():
    while True:
        print("\n- MENU PRINCIPAL -\n")
        for opcao in opcoes_menu:
            print(opcao)

        opcao_escolhida = input("\nDigite uma opção: ")

        match opcao_escolhida:
            case '1':
                listar_contatos.executar()
            case '2':
                criar_contato.executar()
            case '3':
                atualizar_contato.executar()
            case '4':
                deletar_contato.executar()
            case '5':
                print("\nPrograma encerrado.")
                break
            case _:
                print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    system('clear')
    print("\n" + datetime.now().strftime("%d/%m/%Y, %H:%M"))
    iniciar_menu()
