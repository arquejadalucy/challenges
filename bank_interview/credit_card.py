class CreditCard:
    emissor: str
    accout_number: str
    filler: str

    def __init__(self, emissor: str, accout_number: str, filler: str):
        self.emissor = emissor
        self.accout_number = accout_number
        self.filler = filler