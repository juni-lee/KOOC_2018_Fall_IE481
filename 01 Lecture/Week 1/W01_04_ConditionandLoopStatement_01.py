numScore = 75
if numScore > 90:
    print("A")
elif numScore > 80:
    print("B")
elif numScore > 70:
    print("C")
else:
    print("D or F")

print()

for itr in range(10):
    print(itr)

print()

sum = 0
for itr in range(1,11):
    sum += itr
print(sum)

print()

for itr in range(1,100,10):
    if itr == 51:
        continue  # 제일 위의 for으로 다시 돌아가라
    else:
        print(itr)

print()

for itr in range(5):
    # if itr == 4:
    #     break  # for loop의 밖으로 나가라
    print(itr)
else:  # for loop가 break나 다른 error 없이 잘 끝났을 때, for loop가 끝나고 else를 실행시킴
    print("!")
print("done")

print()

for idx in range(2):
    for itr in range(5):
        if itr == 4:
            break  # break는 현재 for loop에서만 밖으로 나간다.
        print(itr)
    print(idx)