"""
Overriding Methods in object
    All of Python classes are the descendants of object
        If you don't specify the base class of your class, then your class is the direct derived class of object
    object has many hidden methods
        __init__ : constructor
        __del__ : destructor
        __eq__ : equality 비교, 메모리 장소를 비교하지는 않고, 단지 값을 비교. == 와 같음
        __cmp__ : compare
        __add__
    you override them to make the methods behave as you please
"""

class Room():
    numWidth = 100
    numHeight = 100
    numDepth = 100
    def __init__(self,parWidth,parHeight,parDepth):
        self.numWidth = parWidth
        self.numHeight = parHeight
        self.numDepth = parDepth
    def getVolume(self):
        return self.numWidth * self.numHeight * self.numDepth
    def __eq__(self, other):
        if isinstance(other,Room):
            if self.getVolume() == other.getVolume():
                return True
        return False

room1 = Room(100,20,30)
room2 = Room(100,10,60)
print(room1.getVolume())
print(room2.getVolume())
print(room1 == room2)  # class의 instance끼리 equality 비교
room3 = Room(100,10,10)
print(room3.getVolume())
print(room1 == room3)
print(room1 == room2 == room3)