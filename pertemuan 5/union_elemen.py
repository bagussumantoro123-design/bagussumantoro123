hobbits = {'frodo', 'sam', 'merry', 'pippin'}
dunedain = {'aragorn'}
elf = {'legolas'}
dwarf = {'gimli'}
human = {'boromir'}
maiar = {'gandalf'}

fellowship_1 = hobbits.union(dunedain).union(elf).union(dwarf).union(human).union(maiar)
print("fellowship_1:", fellowship_1)
# output ➜ fellowship_1: {'boromir', 'gimly', 'legolas', 'pippin', 'sam', 'aragorn', 'frodo', 'gandalf', 'merry'}