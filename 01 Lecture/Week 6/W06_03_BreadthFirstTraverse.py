"""
Queue-based level-order traverse
    Enqueue the root
        While until queue is empty
            Current = Dequeue one element
            Print current
            If Current's LHS exist
                Enqueue current LHS
            If Current's RHS exist
                Enqueue current RHS
"""

def traverseLevelOrder(self):
    ret = []
    Q = Queue()
    Q.enqueue(self.root)

    while Q.isEmpty() == False:
        node = Q.dequeue()
        if node == '':
            continue
        ret.append(node.getValue())
        if node.getLHS() != '':
            Q.enqueue(node.getLHS())
        if node.getRHs() != '':
            Q.enqueue(node.getRHS())

    return ret