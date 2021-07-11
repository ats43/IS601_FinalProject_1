from src.Calculator.Addition import addition
from src.Calculator.Division import division


def mean(data):
    total = 0
    length = len(data)
    for num in data:
        total = addition(total, num)
        return division(total, length)

