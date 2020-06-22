from ProductionList import ProductionList

waitingProduct = ProductionList('Plan-2012.12.24.csv')
print()
print(waitingProduct.nodeHead.nextNode.strModel)
