list_3 = [10, 70, 20, 70]

x = list_3.pop(2)
print('list_3:', list_3)
# output -> list_3: [10, 70, 70]
print('removed element:', x)
# output -> removed element: 20

# index tidak ditemukan -> IndexError
list_3 = [10, 70, 20, 70]
try:
    x = list_3.pop(7)
except IndexError as e:
    print("IndexError:", e)
# output -> IndexError: pop index out of range