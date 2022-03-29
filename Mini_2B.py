list = [12, 75, 150, 180, 145, 525, 50]
a = 5
i = 0
while(i<len(list)):

    if list[i] > 500:
        i += 1
        break
    elif list[i] > 150:
        i += 1
        continue
    elif list[i] % a == 0:
        print(list[i])
    i += 1