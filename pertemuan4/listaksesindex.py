list_1 = [10, 70, 20]

elem_1st = list_1[0]
elem_2nd = list_1[1]
elem_3rd = list_1[2]

print(elem_1st, elem_2nd, elem_3rd)
# output -> 10 70 20

# index di luar kapasitas -> error
try:
    print(list_1[3])
except IndexError as e:
    print("IndexError:", e)
# output -> IndexError: list index out of range