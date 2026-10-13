def aggregate(message, numbers, f):
    res = f(numbers)
    print(f"{message} is {res}")


def avg(numbers):
    return sum(numbers) / len(numbers)