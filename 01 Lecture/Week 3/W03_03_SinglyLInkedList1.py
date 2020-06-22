"""
One variable's value is changed
But, you see three changes
Why this happened?
    Because of references
    x has two references from y and z
    The values of y and z are determined by x, and x is changed
        See the ripple effects
==
    Checks the equivalence of two referenced values
is
    Checks the equivalence of two referenced objects'IDs
"""

""" Basic Structure: Singly linked list
Construct a singly linked list with nodes and references
    A node consists of
        A variable to hold a reference to its next node
        A variable to hold a reference to its value object
    Special nodes: Head and Tail
        You can construct the singly linked list without them
        But, using them makes search, insert and delete more convenient
    Generally, requires more coding than array
"""

""" Implementation of Node class
Member variables
    Variable to reference the next node
    Variable to hold a value object
    (Optional) Variable to check whether it is a head or not
    (Optional) Variable to check whether it is a tail or not
Member functions
    Various get/get methods
"""

""" Basic Structure: Singly linked list
Construct a singly linked list with nodes and references
    A node consists of
        A variable to hold a reference to its next node
        A variable to hold a reference to its value object
    Special nodes: Head and Tail
        You can construct the singly linked list without them
        But, using them makes search, insert and delete more convenient
    Generally, requires more coding than array
"""

""" Implementation of Node class
Member variables
    Variable to reference the next node
    Variable to hold a value object
    (Optional) Variable to check whether it is a head or not
    (Optional) Variable to check whether it is a tail or not
Member functions
    Various get/get methods
"""

class Node:
    nodeNext = ''
    objValue = ''
    blnHead = False
    blnTail = False
    def __init__(self, objValue = '', nodeNext = '', blnHead = False, blnTail = False):
        self.nodeNext = nodeNext
        self.objValue = objValue
        self.blnHead = blnHead
        self.blnTail = blnTail
    def getValue(self):
        return self.objValue
    def setValue(self, objValue):
        self.objValue = objValue
    def getNext(self):
        return self.nodeNext
    def setNext(self, nodeNext):
        self.nodeNext = nodeNext
    def isHead(self):
        return self.blnHead
    def isTail(self):
        return self.blnTail


node1 = Node(objValue = 'a', nodeNext = 'b')
nodeTail = Node(blnTail = True)
nodeHead = Node(blnHead = True, nodeNext = node1, objValue = 'c')
print(node1.objValue)  # node1의 objValue
print(node1.nodeNext)  # node1의 nodeNext
print(nodeHead.nodeNext)  # nodeHead의 nodeNext는 node1
print(nodeHead.nodeNext.objValue)  # nodeHead의 nodeNext는 node1이기 때문에, node1의 objValue
print(nodeHead.nodeNext.nodeNext)  # nodeHead의 nodeNext(node1의 nodeNext
print(nodeHead.objValue)  # nodeHead의 objValue