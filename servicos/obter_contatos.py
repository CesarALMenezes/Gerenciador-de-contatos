import csv

def executar():
    """Obtém os contatos do arquivo CSV."""
    try:
        with open("dados/contatos.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            return [linha for linha in leitor]
    except FileNotFoundError:
        print("Arquivo de contatos não encontrado. Retornando lista vazia.")
        return []
