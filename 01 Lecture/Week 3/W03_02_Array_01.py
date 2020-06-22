""" Creating a List by Array
Array
    Each element is accessible by index
    Index is typically zero or a positive integer
    Very simple creation
        That's why people use it
"""

x = ['a', 'b', 'c', 'd', 'e']
for i in range(len(x)):
    if x[i] == 'c':
        print(i); break;

print()


""" Insert procedure in array
Let's insert 'c' between 'b' and 'd' in the list
"""

x = ['a', 'b', 'd', 'e', 'f']
idxInsert = 2
valInsert = 'c'

y = list(range(6))
print(y)

for itr in range(0,idxInsert):
    y[itr] = x[itr]
print(y)

y[idxInsert] = valInsert
print(y)

for itr in range(idxInsert, len(x)):
    y[itr+1] = x[itr]
print(y)


""" Problems in Array
Whenever you put something in or get something out
    You have to perform line-wise retrievals
        Which is N retrievals
    This process is just like that
        there is a line of airline passengers
        You want to put a passenger in the middle of the line because his flight is about to leave
        You are moving all the passengers one step back
        Then, you put the customer in the line
    What-if we have a magic to create a space in the middle of the line?
        Array -> you are bounded to the 1-dimension that you have
        Linked list -> you are bounded no more!
"""