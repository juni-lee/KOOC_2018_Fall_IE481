import numpy as np

f = open('Plan-2012.12.17.csv')
temp = f.readlines()
print(temp)
f.close()

dataset = [row[:-1].split(',') for row in temp]
# dataset = []
# for row in temp:
#     dataset.append(row[:-1].split(','))
print(dataset)
Dataset = np.asarray(dataset[1:]).T
print(Dataset)

numNos = Dataset[0].astype('int')
print(numNos)
strSerialNumbers = Dataset[1].astype('str')
print(strSerialNumbers)
print(strSerialNumbers[0])
print(strSerialNumbers[1])
# strModels = Dataset[2].astype('str')
# numModelNumbers = Dataset[3].astype('int')
# dateStart = Dataset[4].astype('str')
# numAssemblyOrders = Dataset[5].astype('int')
# dateEnd = Dataset[6].astype('str')
# strOrderOrigins = Dataset[7].astype('str')