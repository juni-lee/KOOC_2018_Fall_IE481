def enqueueWithPriority(self, value, priority):
    self.arrPriority[self.size] = priority
    self.arrValue[self.size] = value
    self.size = self.size + 1
    self.percorlateUp(self.size-1)

def percorlateUp(self, idxPercolate):
    if idxPercolate == 0:
        return
    parent = int((idxPercolate-1) / 2)
    if self.arrPriority[parent] < self.arrPriority[idxPercolate]:
        self.arrPriority[parent], self.arrPriority[idxPercolate] = self.arrPriority[idxPercolate], self.arrPriority[parent]
        self.arrValue[parent], self.arrValue[idxPercolate] = self.arrValue[idxPercolate], self.arrValue[parent]
        self.percorlateUp(parent)


