"""
Polymorphism
    Poly: Many
    Morph: Shape
    Different behaviors with similar signature
        Signature = Method name + Parameter list
    Method Overriding
        Base class has a method A(num), and its derived class has a method A(num)
    Method Overloading
        A class has a method A(num), A(num,name), and A(num,name,home)
"""

class Building():
    strAddress = "Daejeon"
    def openDoor(self):
        print("Door opened")

class Hotel():
    def openDoor(self):
        print("Bellboy opens a door")
    def checkIn(self):
        print("Someone checks in for 1 day")
    def checkIn(self,days):
        print("Someone checks in for", days, "days")

lotteHotel = Hotel()
lotteHotel.openDoor()
lotteHotel.checkIn()
# lotteHotel.checkIn(2)