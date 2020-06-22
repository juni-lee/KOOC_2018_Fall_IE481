""" Head and Tail
Specialized node
    Head : Always at the first of the list
    Tail : Always at the last of the list
    These are the two corner stone showing the start and the end of the list
These are optional nodes
    Linked list works okay without these
    However, having these makes implementation very convenient
    Any example?
"""

""" Search procedure in singly linked list
Again, let's find 'd' and 'c' from the list
Just like an array, navigating from the first to the last until hit is the only way
No difference in the search pattern, though you cannot use index any further!
    Your list implementation may include the index function, but it is not required in the linked list
"""

""" Insert procedure in singly linked list
This is the moment that you see the power of a linked list
Last time, you need N retrievals to insert a value in the array list
This time, you need only three operations
    With an assumption that you have a reference to the node, Node(prev) that you want to put your new node next
    First, you store a Node, or a Node(next), pointed by a reference from Node(prev)'s nodeNext member variable
    Second, you change a reference from Node(prev)'s nodeNext to Node(new)
    Third, you change a reference from Node(new)'s nodeNext to Node(next)
"""

""" Delete procedure in singly linked list
This is the another moment that you see the power of a linked list
Last time, you need N retrievals to delete a value in the array list
This time, you need only three operations
    With an assumption that you have a reference to the node, Node(prev) that you want to remove the node next
    First, you retrieve Node(next) that is two steps next from Node(prev)
    Second, you change a reference from Node(prev)'s nodeNext to Node(next)
The node will be removed because there is no reference to Node(remove)
"""

from W03_03_Class_Node import *

class SinglyLinkedList():
    nodeHead = ''
    nodeTail = ''
    size = 0
    def __init__(self):
        self.nodeHead = Node(blnHead = True, nodeNext = self.nodeTail)
        self.nodeTail = Node(blnTail = True)

    def insertAt(self, objInsert, idxInsert):
        nodeNew = Node(objValue = objInsert)
        nodePrev = self.get(idxInsert - 1)
        nodeNext = nodePrev.getNext()
        nodePrev.setNext(nodeNew)
        nodeNew.setNext(nodeNext)
        self.size = self.size + 1

    def removeAt(self, idxRemove):
        nodePrev = self.get(idxRemove - 1)
        nodeRemove = nodePrev.getNext()
        nodeNext = nodeRemove.getNext()
        nodePrev.setNext(nodeNext)
        self.size = self.size - 1
        return nodeRemove.getValue()

    def get(self, idxRetrieve):
        nodeReturn = self.nodeHead
        for itr in range(idxRetrieve + 1):
            nodeReturn = nodeReturn.getNext()
        return nodeReturn

    def printStatus(self):
        nodeCurrent = self.nodeHead
        while nodeCurrent.getNext().isTail() == False:
            nodeCurrent = nodeCurrent.getNext()
            print(nodeCurrent.getValue(), end = ' ')
        print()

    def getSize(self):
        return self.size


list1 = SinglyLinkedList()
list1.insertAt('a', 0)
list1.insertAt('b', 1)
list1.insertAt('d', 2)
list1.insertAt('e', 3)
list1.insertAt('f', 4)
list1.printStatus()

list1.insertAt('c', 2)
list1.printStatus()

list1.removeAt(3)
list1.printStatus()