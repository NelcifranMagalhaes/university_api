def cpf_invalid(cpf):
    return len(cpf) !=11

def name_invalid(name):
    return not name.isalpha()

def phone_invalid(phone):
    return len(phone) !=13