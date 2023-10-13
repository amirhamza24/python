# break

list1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

for x in range(len(list1)):
    if x == 4:
        break
    print(x)  # output: 0 1 2 3 [egulo index number]


list2 = [ "apple", "orange", "mango", "cherry", "kiwi", "banana" ]

for x in range(len(list2)):
    if x == 4:
        break
    print(x)  # output: 0 1 2 3 [egulo index number]


# continue

list1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

for x in range(len(list1)):
    if x == 4:
        continue
    print(x)  # output: 0 1 2 3 5 6 7 8 [egulo index number, ekhane 4 ashbena, cause continue use korechi]