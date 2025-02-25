class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def __add__(self, other):
        if isinstance(self, Money) and isinstance(other, Money):
            if self.currency == other.currency:
                return Money(self.amount + other.amount, self.currency)
            else:
                raise RuntimeError("Not the same currency")
        else:
            raise ValueError(f"Can only add Money to Money")
    
    def __sub__(self, other):
        if isinstance(self, Money) and isinstance(other, Money):
            if self.currency == other.currency:
                return Money(self.amount - other.amount, self.currency)
            else:
                raise RuntimeError("Not the same currency")
        else:
            raise ValueError(f"Can't only subtract Money from Money")
    
    def __mul__(self, other):
        if isinstance(self, Money) and isinstance(other, (int, float)):
            return Money(self.amount * other, self.currency)
        else:
            raise ValueError(f"Can only multiple Money with int or float")