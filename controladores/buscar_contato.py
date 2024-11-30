from servicos import obter_contatos

def executar():
   
    contatos = obter_contatos.executar()
    if not contatos:
        print("Nenhum contato encontrado.")
        return
    
    criterio = input("Digite o nome, telefone, email ou empresa para buscar: ").strip().lower()
    resultados = [
        contato for contato in contatos
        if criterio in contato["nome"].lower()
        or criterio in contato["telefone"]
        or criterio in contato["email"].lower()
        or criterio in contato["empresa"].lower()
    ]
    
    if resultados:
        print("\n--- Resultados da Busca ---")
        for contato in resultados:
            print(f"ID: {contato['id']}, Nome: {contato['nome']}, Telefone: {contato['telefone']}, "
                  f"E-mail: {contato['email']}, Empresa: {contato['empresa']}, Aniversário: {contato['aniversario']}")
    else:
        print("Nenhum contato correspondente foi encontrado.")
