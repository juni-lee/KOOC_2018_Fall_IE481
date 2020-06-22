def FibonacciDP(n):
    dicFibonacci = {}
    dicFibonacci[0] = 0
    dicFibonacci[1] = 1
    for itr in range(2,n+1):
        dicFibonacci[itr] = dicFibonacci[itr-1] + dicFibonacci[itr-2]
    return dicFibonacci[n]

for itr in range(0,10):
    print(FibonacciDP(itr))

"""
Use a dictionary collection variable type for memoization
    Memoization
        Storing a fibonacci number for a particular index
Now,
    We have a new space requirement, the dictionary or the table, of O(N)
    We have reduced execution time from O(2^n) to O(N)
"""