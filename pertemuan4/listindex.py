list_2 = ['ab', 'cd', 'hi', 'ca']

idx_1st = list_2.index('cd')
print('idx_1st: ', idx_1st)
# output -> idx_1st:  1

# element tidak ada -> ValueError
try:
    idx_2nd = list_2.index('kk')
    print('idx_2nd: ', idx_2nd)
except ValueError as e:
    print("ValueError:", e)
# output -> ValueError: 'kk' is not in list