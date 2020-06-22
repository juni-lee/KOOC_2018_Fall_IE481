
class Building():
    strAddress = "Daejeon"
    def openDoor(self):
        print("Door opened")

class Hotel(Building):
    def openDoor(self):
        print("Building opens a door")
    def checkIn(self, days = 1):
        print("Someone checks in for", days, "days")

lotteHotel = Hotel()
lotteHotel.openDoor()
lotteHotel.checkIn()
lotteHotel.checkIn(2)