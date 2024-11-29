import csv

def executar(contatos):
    """Atualiza todos os contatos no arquivo CSV."""
    cabecalho = ["id", "nome", "telefone", "email", "empresa", "aniversario"]
    try:
        with open("dados/contatos.csv", "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)
            escritor.writeheader()
            escritor.writerows(contatos)
        return True
    except Exception as e:
        print(f"Erro ao atualizar contatos: {e}")
        return False
