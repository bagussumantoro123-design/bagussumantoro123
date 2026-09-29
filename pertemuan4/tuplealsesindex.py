tuple_1 = (2, 3, 4, 5)

print("elem 0:", tuple_1[0])
# output -> elem 0: 2

print("elem 1:", tuple_1[1])
# output -> elem 1: 3

# index di luar kapasitas -> IndexError
try:
    print("elem 4:", tuple_1[4])
except IndexError as e:
    print("IndexError:", e)
# output -> IndexError: tuple index out of range