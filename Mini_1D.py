def merge(list1, list2):
    mergedlist = tuple(zip(list1, list2))
    return mergedlist
list1 = [19542209, 4887871, 1420491, 626299, 1805832, 39865590]
list2 = ["New York", "Alabama", "Hawaii", "Vermont", "West Virginia",  "California"]
print(merge(list1, list2))