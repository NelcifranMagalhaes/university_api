import re

def cpf_invalid(cpf):
    return len(cpf) !=11

def name_invalid(name):
    return not name.isalpha()

def phone_invalid(phone):
    # 86 99999-9999
    regex_model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    response = re.findall(regex_model,phone)
    return not response