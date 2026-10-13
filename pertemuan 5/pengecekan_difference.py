fellowship = {'aragorn', 'gimli', 'legolas', 'gandalf', 'boromir', 'frodo', 'sam', 'merry', 'pippin'}
hobbits = {'frodo', 'sam', 'merry', 'pippin', 'bilbo'}

diff = fellowship.difference(hobbits)
print("diff:", diff)
# output ➜ diff: {'boromir', 'legolas', 'aragorn', 'gimli', 'gandalf'}

fellowship.difference_update(hobbits)
print("fellowship:", fellowship)
# output ➜ fellowship: {'boromir', 'legolas', 'aragorn', 'gimli', 'gandalf'}