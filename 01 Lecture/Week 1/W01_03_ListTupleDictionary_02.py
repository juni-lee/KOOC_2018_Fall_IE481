"""
Dictionary
    Dictionary is also a collection variable type
        However, it is not sequential
        It works by a pair of keys and values
            A set of (key 1, value 1), (key 2, value 2), (key 3, value 3)...
            Exact syntax is {key1:value1, key2:value2, key3:value3 ...)
"""

dicTest = {1:'one', 2:'two', 3:'three'}
print(dicTest[1])
# print(dicTest[4])
dicTest[4] = 'four'  # 이런 식으로 items(key와 value)를 추가할 수 있구나
print(dicTest)
dicTest[100] = 'hundred'  # item은 순서를 고려하지 않아도 되는구나
print(dicTest)
dicTest[1] = 'hana'  # 이런 식으로 key의 value를 새롭게 바꿀 수 있구나
print(dicTest)
print(dicTest.keys())
print(dicTest.values())
print(dicTest.items())