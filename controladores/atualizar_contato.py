from funcionalidades import atualizar_contato

def executar():
    id_contato = input("Informe o ID do contato: ")

    if not id_contato.isnumeric():
        print("ID inválido.")
        return

    atualizar_contato.executar(id_contato)
