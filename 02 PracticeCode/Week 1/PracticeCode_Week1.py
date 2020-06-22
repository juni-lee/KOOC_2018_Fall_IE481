v1 = [1,2,3]
v2 = [4,5,6]
for x,y in zip(v1,v2):
    print((x,y))

v1 = ['a','b','c']
for index,value in enumerate(v1):
    print(index,value)

v = [1,2,3,4,5]
print(sum(v))

v1 = [[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12]]

v2 = [sum(row) for row in v1]
print(v2)