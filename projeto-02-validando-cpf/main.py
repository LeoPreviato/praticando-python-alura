def validar_cpf(cpf):
    if not cpf.isdigit():
        return("ERRO: O CPF deve conter apenas números.")
    if len(cpf) < 11:
        return("ERRO: O CPF deve conter exatamente 11 números")
    return "CPF válido."

cpf = input("Digite seu CPF: ")

print(validar_cpf(cpf))
