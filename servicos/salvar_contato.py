import csv

def executar(contato):
    """Salva um novo contato no arquivo CSV."""
    cabecalho = ["id", "nome", "telefone", "email", "empresa", "aniversario"]
    try:
        with open("dados/contatos.csv", "a", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)
            if arquivo.tell() == 0:  # Verifica se o arquivo está vazio
                escritor.writeheader()
            escritor.writerow(contato)
        return True
    except Exception as e:
        print(f"Erro ao salvar contato: {e}")
        return False
