from funcionalidades.utilidades import validar_email, validar_data
from servicos import obter_proximo_id_contato, salvar_contato

def executar():
    print("\n** Cadastro de Novo Contato **")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = validar_email.executar(input("E-mail: "))
    empresa = input("Empresa: ")
    aniversario = validar_data.executar(input("Data de Aniversário (DD/MM/YYYY): "))

    novo_contato = {
        "id": obter_proximo_id_contato.executar(),
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "empresa": empresa,
        "aniversario": aniversario,
    }

    if salvar_contato.executar(novo_contato):
        print("Contato salvo com sucesso!")
    else:
        print("Erro ao salvar contato.")
