"""
Depth first traverse
    Pre-order traverse
        Order: Current, LHS, RHS in Recursion
    In-order traverse
        Order: LHS, Current, RHS in Recursion
    Post-order traverse
        Order: LHS, RHS, Current in Recursion
"""


def traversePreOrder(self, node = ''):
    if node == '':
        node = self.root
    ret = []

    ret.append(node.getValue())
    if node.getLHS() != '':
        ret = ret + self.traversePreOrder(node.getLHS())
    if node.getRHS() != '':
        ret = ret + self.traversePreOrder(node.getRHS())
    return ret


def traverseInOrder(self, node = ''):  # 정렬된 sorting의 결과와 동일
    if node == '':
        node = self.root
    ret = []

    if node.getLHS() != '':
        ret = ret + self.traverseInOrder(node.getLHS())
    ret.append(node.getValue())
    if node.getRHS() != '':
        ret = ret + self.traverseInOrder(node.getRHS())
    return ret


def traversePostOrder(self, node = ''):
    if node == '':
        node = self.root
    ret = []

    if node.getLHS() != '':
        ret = ret + self.traverseInOrder(node.getLHS())
    if node.getRHS() != '':
        ret = ret + self.traverseInOrder(node.getRHS())
    ret.append(node.getValue())
    return ret
