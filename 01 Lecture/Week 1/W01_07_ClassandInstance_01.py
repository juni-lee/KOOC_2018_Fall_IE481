"""

"""

class MyHome:
    colorRoof = 'red'
    stateDoor = 'closed'
    def paintRoof(self,color):
        self.colorRoof = color
    def openDoor(self):
        self.stateDoor = 'open'
    def closeDoor(self):
        self.stateDoor = 'close'
    def printStatus(self):
        print("Roof color is", self.colorRoof + ",",
              "and door is", self.stateDoor)

homeAtDaejeon = MyHome()
homeAtSeoul = MyHome()
print(homeAtDaejeon.colorRoof)
homeAtSeoul.openDoor()
homeAtDaejeon.paintRoof('blue')
homeAtDaejeon.printStatus()
homeAtSeoul.printStatus()
