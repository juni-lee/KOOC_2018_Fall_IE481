strTest = 'Hello World! ISE'

print(strTest)
print(strTest[1],strTest[2],strTest[3])
print(strTest[1:3])
print(strTest[3:])
print(strTest[:3])
print(strTest[1:9:2])
print(strTest[1:len(strTest):2])
print(strTest[:len(strTest)])
print(strTest[1::2])
print(strTest[5::-1])

print()

lstTest = [1,2,3,4]
print(lstTest + lstTest)
print(lstTest*3)

print()

# range(x,y,z) == x:y:z
lstTest = list(range(1,20,3))  # [1,4,7,10,13,16,19]
print(lstTest)
print(4 in lstTest, 100 in lstTest, 100 not in lstTest)  # 4가 lstTest에 있으니까 True, 100은 없으니까 False
lstTest.append('hey')  # list 맨 뒤에 'hey'를 추가한다
print(lstTest)
del(lstTest[0])  # 0번째를 지운다
print(lstTest)
lstTest.reverse()  # 순서를 거꾸로 뒤집는다
print(lstTest)
lstTest.remove('hey')  # 'hey'를 모두 지운다
print(lstTest)
lstTest.sort()  # 작은 것부터 순서대로 나열한다
print(lstTest)
lstTest[0] = 100
print(lstTest)

print()

"""
Tuple
    Tuple and List are almost alike
    Only different in changing values
        Tuple does not allow value changes
"""

tplTest = (1,2,3)
print(tplTest)
print(tplTest[0], tplTest[1])
print(tplTest[1:3])
print(tplTest + tplTest)
print(tplTest * 3)
tplTest[0] = 100
print(tplTest)  # 윗줄의 error 때문인지 프린트가 되지 않음