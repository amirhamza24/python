# you can loop through the list item by using a for loop
loopList = ["rakib", "rohim", "korim", "sojib", "jahin"]
for nam in loopList:
    print(nam)


# use the range() and len() functions to create a suitable iterable. mane ami j list ba array nibo setar size ba index print korbe
for i in range(len(loopList)):
    print(i)

# print all item using a while loop to go through all the index numbers.
y = 0
while y < len(loopList):
    print(loopList[y])
    y = y + 1

    