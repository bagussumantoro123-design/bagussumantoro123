list_x = ['a', 'b', 'c']
list_y = ['1', '2', '3']

# perulangan bersarang
seq = []
for x in list_x:
    for y in list_y:
        seq.append(x + y)

print(seq)
# output -> ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

# list comprehension
seq = [x + y for x in list_x for y in list_y]

print(seq)
# output -> ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']