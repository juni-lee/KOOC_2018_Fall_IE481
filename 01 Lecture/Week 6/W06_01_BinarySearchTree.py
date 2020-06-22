def insert(self, value, node = ''):
    if node == '':
        node = self.root
    if self.root == '':
        self.root = TreeNode(value, '')
    if value == node.getValue():
        return
    if value > node.getValue():
        if node.getRHS() == '':
            node.setRHS(TreeNode(value, node))
        else:
            self.insert(value, node.getRHS())
    if value < node.getValue():
        if node.getLHS() == '':
            node.setLHS(TreeNode(value, node))
        else:
            self.insert(value, node.getLHS())
    return


def search(self, value, node = ''):
    if node == '':
        node = self.root
    if value == node.getValue():
        return True
    if value > node.getValue():
        if node.getRHS() == '':
            return False
        else:
            return self.search(value, node.getRHS())
    if value < node.getValue():
        if node.getLHS() == '':
            return False
        else:
            return self.search(value, node.getLHS())


def delete(self, value, node = ''):
    if node == '':
        node = self.root
    if node.getValue() < value:
        return self.delete(value, node.getRHS())
    if node.getValue() > value:
        return self.delete(value, node.getLHS())
    if node.getValue() == value:
        if node.getLHS() != '' and node.getRHS() != '':
            nodeMin = self.findMin(node.getRHS())
            node.setValue(nodeMin.getValue())
            self.delete(nodeMin.getValue(), node.getRHS())
            return
        parent = node.getParent()
        if node.getLHS() != '':
            if node == self.root:
                self.root = node.getLHS()
            elif parent.getLHS() == node:
                parent.setLHS(node.getLHS())
                node.getLHS().setParent(parent)
            else:
                parent.setRHS(node.getLHS())
                node.getLHS().setParent(parent)
            return
        if node.getRHS() != '':
            if node == self.root:
                self.root = node.getRHS()
            elif parent.getLHS() == node:
                parent.setLHS(node.getRHS())
                node.getRHS().setParent(parent)
            else:
                parent.setRHS(node.getRHS())
                node.getRHS().setParent(parent)
            return
        if node == self.root:
            self.root = ''
        elif parent.getLHS() == node:
            parent.setLHS('')
        else:
            parent.setRHS('')
        return


def findMax(self, node = ''):
    if node == '':
        node = self.root
    if node.getRHS() == '':
        return node
    return self.findMax(node.getRHS())


def findMin(self, node = ''):
    if node == '':
        node = self.root
    if node.getLHS() == '':
        return node
    return self.findMin(node.getLHS())
