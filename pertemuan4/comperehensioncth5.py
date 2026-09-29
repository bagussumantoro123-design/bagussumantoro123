matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# perulangan biasa
transposed = []
for i in range(4):
    tr = []
    for row in matrix:
        tr.append(row[i])
    transposed.append(tr)

print(transposed)
# output -> [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# list comprehension
transposed = [[row[i] for row in matrix] for i in range(4)]

print(transposed)
# output -> [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]