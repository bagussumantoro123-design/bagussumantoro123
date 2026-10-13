data = {1, 2, 3, 2, 1, 4, 5, 2, 3, 5}
print(data)
# output ➜ {1, 2, 3, 4, 5}
data = [1, 2, 3, 2, 1, 4, 5, 2, 3, 5]
print(data)
# output ➜ [1, 2, 3, 2, 1, 4, 5, 2, 3, 5]
data_unique_set = set(data)
print(data_unique_set)
# output ➜ {1, 2, 3, 4, 5}
data_unique = list(data_unique_set)
print(data_unique)
# output ➜ [1, 2, 3, 4, 5]