
def check_sum(number: str):
    is_valid = True
    sum = 0
    for i in range(0, 16):
        if i == 0 or i % 2 == 0:
            n = int(number[i])*2
            if n >= 10:
                for m in n.:
                    sum += m
        else:
            sum += int(number[i])

    if not is_valid:
        raise Exception("Este cartão de crédito não é válido")

def validate_len(number: str):
    if len(number) == 16:
        raise Exception("Este número não tem o tamanho correto")

def validate_numeric(number: str):
    digits = str(1234567890)
    for char in number:
        if char not in digits:
            raise Exception("A entrada deve conter apenas números")