a = set('abracadabra') # {'c', 'a', 'r', 'd', 'b'}
b = set('alacazam')     # {'c', 'z', 'a', 'm', 'l'}

res = a ^ b
print(res)
# output ➜ {'z', 'r', 'b', 'd', 'm', 'l'}