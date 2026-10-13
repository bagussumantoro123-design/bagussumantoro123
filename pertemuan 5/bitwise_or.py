a = set('abracadabra') # {'c', 'a', 'r', 'd', 'b'}
b = set('alacazam')     # {'c', 'z', 'a', 'm', 'l'}

res = a | b
print(res)
# output ➜ {'c', 'z', 'a', 'r', 'd', 'b', 'm', 'l'}
