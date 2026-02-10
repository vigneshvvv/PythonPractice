class InsufficientFundException(Exception):
    balance = None
    amount = None
    message = None

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = "InsufficientFund please check you balance"
        super().__init__(self.message)


def withdrawAmount(balance, amount):
    if amount>balance:
        raise InsufficientFundException(balance, amount)
    result = balance - amount
    return result     


try:
    balance = 10000
    # amount = 20000
    amount = int(input("Enter the Amount you wish to withdraw:"))
    newbalance = withdrawAmount(balance, amount)
except InsufficientFundException as e:
    print(e)

