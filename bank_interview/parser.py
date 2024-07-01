import validator
from credit_card import CreditCard


def parse_number(credit_card_number: str):
    """
    :param credit_card_number: número de 16 dígitos
    :return: classe CreditCard
    """
    #exemplo 4417123456789113
    # 441712
    # 345678911
    # 3
    validator.validate_numeric(credit_card_number)
    validator.validate_len(credit_card_number)
    validator.check_sum(credit_card_number)

    emissor = credit_card_number[0:6]
    filler = credit_card_number[-1]
    account_number = credit_card_number[6:15]

    return CreditCard(
        emissor=emissor,
        filler=filler,
        accout_number=account_number
    )
