class Calc:
    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def zero(self, a, b):
        if a or b == 0:
            return "inf"

    def is_empty(self, a):
        if a == []:
            return "is empty"

    def average(selfs, a):

