from servicos import obter_contatos

def executar():
    
    contatos = obter_contatos.executar()
    if not contatos:
        return "1"
    return str(int(max(contato["id"] for contato in contatos)) + 1)
