from servicos import obter_contatos

def executar():
    contatos = obter_contatos.executar()

    if not contatos:
        print("Nenhum contato encontrado.")
        return

    for contato in contatos:
        print("\n--- Contato ---")
        for chave, valor in contato.items():
            print(f"{chave}: {valor}")
