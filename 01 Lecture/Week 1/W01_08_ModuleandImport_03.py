class CashierLine:
    # def __init__(self):
    #     self.lstLine = []

    lstLine = []

    def addCustomer(self,strName):
        self.lstLine.append(strName)

    def processCustomer(self):
        strReturnName = self.lstLine[0]
        self.lstLine.remove(strReturnName)
        return strReturnName

    def printStatus(self):
        strReturn = ""
        for itr in range(len(self.lstLine)):
            strReturn += self.lstLine[itr] + " "
        return strReturn


binLoop = True
line = CashierLine()
while binLoop:
    strName = input("Enter customer name : ")  # input type is string

    if strName == ".":
        break  # go out while loop
    elif strName == "->":
        print(line.lstLine)
        print("Processed :", line.processCustomer())
        print("Line :", line.printStatus())
    else:
        line.addCustomer(strName)
        print(line.lstLine)
        print("Line :", line.printStatus())


print("Number of remaining customer :", len(line.lstLine))