""" Repeating Problems and Divide and Conquer
Can't avoid the below structures
    class Department
        dept = [sales, manu, randd]
        def calculatebudget(self)
            Sum = 0
            for itr in range(0, numDepartments)
                Sum = sum + dept[itr].calculateBudget()
            Return sum
"""

def factorial(n):
    if n == 0:
        result = 1
    elif n > 0:
        result = n * factorial(n-1)
    return result

print(factorial(5))
print()


""" Recursion
A programming method to handle the repeating items in a self-similar way
    Often in a form of
        Calling a function within the function
            def functionA(target)
                functionA(target')
                if (escapeCondition)
                    return A;
"""

def Fibonacci(n):
    if n < 0:
        print("There is an error in 'input'!!!")
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        intRet = Fibonacci(n-1) + Fibonacci(n-2)
    return intRet

print(Fibonacci(10))
for itr in range(0, 10):
    print(Fibonacci(itr))


""" Recursions and Stackframe
Recursion of functions
    Increase the items in the stackframe
        Stackframe is a stack storing your function call history
            Push : When a function is invoked
            Pop : when a function hits return or ends
"""