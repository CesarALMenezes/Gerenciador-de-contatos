from datetime import datetime

def executar(data_str):
    
    try:
        return datetime.strptime(data_str, "%d/%m/%Y").strftime("%d/%m/%Y")
    except ValueError:
        print("Data inválida. Tente novamente.")
        return executar(input("Data de Aniversário (DD/MM/YYYY): "))
