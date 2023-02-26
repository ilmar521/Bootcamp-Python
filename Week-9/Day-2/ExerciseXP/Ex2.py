
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f'{self.amount} {self.currency}{"s" if self.amount > 1 else ""}'

    def __int__(self):
        return self.amount

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, Currency):
            if other.currency != self.currency:
                raise Exception(f'Cannot add between Currency type {self.currency} and {other.currency}')
            self.amount += other.amount
        elif isinstance(other, int):
            self.amount += other

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if other.currency != self.currency:
                raise Exception(f'Cannot add between Currency type {self.currency} and {other.currency}')
            self.amount += other.amount
            return self
        elif isinstance(other, int):
            self.amount += other
            return self


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(str(c3))

print(int(c1))
print(repr(c1))
c1 + 5
print(c1)
c1 + c2
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
c1 + c3



