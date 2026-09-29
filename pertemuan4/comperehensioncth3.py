# perulangan biasa + ternary
seq = []
for i in range(1, 10):
    seq.append(i * (2 if i % 2 == 0 else 3))

print(seq)
# output -> [3, 4, 9, 8, 15, 12, 21, 16, 27]

# list comprehension
seq = [(i * (2 if i % 2 == 0 else 3)) for i in range(1, 10)]

print(seq)
# output -> [3, 4, 9, 8, 15, 12, 21, 16, 27]