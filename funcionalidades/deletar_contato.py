from servicos import obter_contatos, atualizar_contatos

def executar(id_contato):
    contatos = obter_contatos.executar()
    contatos_filtrados = [c for c in contatos if c["id"] != id_contato]

    if len(contatos) == len(contatos_filtrados):
        print("Contato não encontrado.")
        return

    if atualizar_contatos.executar(contatos_filtrados):
        print("Contato excluído com sucesso!")
    else:
        print("Erro ao excluir contato.")
