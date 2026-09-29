list_1 = [10, 70, 20]
print('before: ', list_1)
# output -> before:  [10, 70, 20]

list_1[len(list_1):] = [88, 87]
print('after: ', list_1)
# output -> after:  [10, 70, 20, 88, 87]