from datetime import datetime

def executar(data_str):
    """Valida se a data está no formato DD/MM/YYYY."""
    try:
        return datetime.strptime(data_str, "%d/%m/%Y").strftime("%d/%m/%Y")
    except ValueError:
        print("Data inválida. Tente novamente.")
        return executar(input("Data de Aniversário (DD/MM/YYYY): "))
