from servicos import obter_contatos, atualizar_contatos

def executar(id_contato):
    contatos = obter_contatos.executar()
    contato_atualizado = None

    for contato in contatos:
        if contato["id"] == id_contato:
            contato_atualizado = contato
            break

    if not contato_atualizado:
        print("Contato não encontrado.")
        return

    print("\n--- Atualizar Contato ---")
    for chave, valor in contato_atualizado.items():
        if chave == "id":
            continue

        novo_valor = input(f"{chave} (atual: {valor}): ")
        if novo_valor:
            contato_atualizado[chave] = novo_valor

    if atualizar_contatos.executar(contatos):
        print("Contato atualizado com sucesso!")
    else:
        print("Erro ao atualizar contato.")
