# perulangan biasa
seq = []
for i in range(10):
    if i % 2 == 1:
        seq.append(i)

print(seq)
# output -> [1, 3, 5, 7, 9]

# list comprehension
seq = [i for i in range(10) if i % 2 == 1]

print(seq)
# output -> [1, 3, 5, 7, 9]