def aggregate(message, numbers, f):
    res = f(numbers)
    print(f"{message} is {res}")


def avg(numbers):
    return sum(numbers) / len(numbers)


numbers = [24, 67, 22, 98, 3, 50]

aggregate("total", numbers, sum)
aggregate("average", numbers, avg)
aggregate("maximum", numbers, max)
aggregate("minimum", numbers, min)