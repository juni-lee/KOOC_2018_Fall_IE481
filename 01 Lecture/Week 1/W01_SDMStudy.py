def main():
    numYear = 2011

    print("Year by base 10 : %d, by base 8 : %o, by base 16 : %X" %(numYear,numYear,numYear))

main()


dicTest = {1:'one', 2:'two', 3:'three'}
print(dicTest[1])
print(dicTest)
dicTest[1] = 'hana'
print(dicTest)
print(dicTest.keys())
print(dicTest.values())
print(dicTest.items())