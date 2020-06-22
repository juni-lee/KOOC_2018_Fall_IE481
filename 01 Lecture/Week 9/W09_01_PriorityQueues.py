import sys
sys.path.append("C:\\Users\SDM-LEEJUNHUI\Dropbox\KAIST_Individual\Programming\PythonAndMatlab\KOOC_2018 Fall IE481\\01 Lecture\Week 3")
from W03_03_Class_SinglyLinkedList import *


class PriorityNode:
    priority = -1
    value = ''

    def __init__(self, value, priority):
        self.priority = priority
        self.value = value

    def getValue(self):
        return self.value

    def getPriority(self):
        return self.priority


class PriorityQueue:

    list = ''

    def __init__(self):
        self.list = SinglyLinkedList()

    def enqueueWithPriority(self, value, priority):
        idxInsert = 0
        for itr in range(self.list.getSize()):
            node = self.list.get(itr)
            if node.getValue() == '':
                idxInsert = itr
                break
            if node.getValue().getPriority() < priority:  # priority가 높으면 앞쪽에 위치한다.
                idxInsert = itr
                break
            else:  # priority가 낮을수록 뒤쪽에 위치한다.
                idxInsert = itr + 1
        self.list.insertAt(PriorityNode(value,priority), idxInsert)

    def dequeueWithPriority(self):
        return self.list.removeAt(0).getValue()  # 앞쪽에 있는 것부터 꺼내온다.


pq = PriorityQueue()

pq.enqueueWithPriority('il-chul moon', 1)
a = pq.list.get(0).getValue().getValue()
print(a); print();

pq.enqueueWithPriority('taesik lee', 2)
pq.enqueueWithPriority('hayong shin', 1)
pq.enqueueWithPriority('tae eog lee', 99)

print(pq.dequeueWithPriority())
print(pq.dequeueWithPriority())
print(pq.dequeueWithPriority())
print(pq.dequeueWithPriority())