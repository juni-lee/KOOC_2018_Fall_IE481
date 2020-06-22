"""
We learn the first set of data structures : linked list, stack, and queue
Objectives are
    Understanding the definition of abstract data types
    Firmly understanding how references work
    Understanding various linked list, stack, and queue structures
        Singly linked list, doubly linked list, circular linked list...
        Able to implement a stack and a queue with a list
    Understanding the procedures of linked list, stack, and queue management
        Insert, delete, search...
        Should be able to estimate the number of steps for inserts, deletes, and searches
"""

"""
Abstract Data Types
    An abstract data type (ADT) is an abstraction of a data structure
        An ADT specifies:
            Data stored
            Operations on the data
            Error conditions associated with operations
    Example: ADT modeling a simple stock trading system
        The data stored are buy/sell orders
        The operations supported are
            order buy(stock, shares, price)
            order sell(stock, shares, price)
            void cancel(order)
        Error conditions:
            Buy/sell a nonexistent stock
            Cancel a nonexistent order
"""