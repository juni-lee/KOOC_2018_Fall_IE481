""" Structure for Stack
Stacks are linear like linked lists
    A variation of a singly linked list
Difference
    Voluntarily giving up
        Access to the middle in the linked list
        Only accesses to the first instance in the list
    The first instance in the list
        = The top instance in the stack
An item is inserted or removed from the stack from one end called the "top" of the stack
    This mechanism is called Last-In-First-Out (LIFO)
"""

""" Operation of Stack
Stack operation
    Push
        = Insert an instance at the first in the linked list
        = Put an instance at the top in the stack
    Pop
        = Remove and return an instance at the first in the linked list.
        = Remove and return an instance at the top in the stack
"""

from W03_03_Class_SinglyLinkedList import SinglyLinkedList

class Stack(object):
    lstInstance = SinglyLinkedList()
    def pop(self):
        return self.lstInstance.removeAt(0)
    def push(self, value):
        self.lstInstance.insertAt(value,0)

stack = Stack()
stack.push("a")
stack.push("b")
stack.push("c")

print(stack.pop())
print(stack.pop())
print(stack.pop())