"""

"""

x = [1, 2, 3]
y = [100, x, 120]
z = [x, 'a', 'b']

print('x : ', x)
print('y : ', y)
print('z : ', z)

print()

x[1] = 1717

print('x : ', x)
print('y : ', y)
print('z : ', z)

x = [1, 2, 3]
x2 = [1, 2, 3]

if x == x2:
    print("Values are equivalent")
else:
    print("Values are not equivalent")

if x is x2:
    print("Values are stored at the same place")
else:
    print("Values are not stored at the same place")

if x[1] is y[1][1]:
    print("Values are stored at the same place")
else:
    print("Values are not stored at the same place")
