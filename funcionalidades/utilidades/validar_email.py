import re

def executar(email):
    """Valida o formato do email."""
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        return email
    print("E-mail inválido. Tente novamente.")
    return executar(input("E-mail: "))
