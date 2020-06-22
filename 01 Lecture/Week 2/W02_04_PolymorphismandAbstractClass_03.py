"""
Abstract class, or Abstract Base Class in Python
    A class with an abstract method
    What is the abstract method?
        Method with signature, but with no implementation
        Why use it then?
           I want to have a window here, but I don't know how it will look like, but you should have a window here!
    Abstract class is not a complete implementation, it is more like a half-made produce
    Therefore, you can't make an instance out of it
The concrete class with full implementations and inheriting the abstract class will be a basis for instances
"""

import abc

class Room():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def openDoor(self):
        pass
    @abc.abstractmethod
    def openwindow(self):
        pass

class BedRoom(Room):
    def openDoor(self):
        print("open bedroom door")
    def openWindow(self):
        print("Open bedroom window")

class Lobby(Room):
    def openDoor(self):
        print("Open lobby door")

room1 = BedRoom()
print(issubclass(BedRoom, Room), isinstance(room1, Room), isinstance(room1, BedRoom))

lobby1 = Lobby()
print(issubclass(Lobby, Room), isinstance(lobby1, Room))
