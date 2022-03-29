list1 = [21,5,8,2,1]
list2 = []
num = 0
while(num < len(list1)):
    if list1[num] % 2 == 0:
        list2.append(list1[num])
    num += 1

print("Smallest even number is:", min(list2))