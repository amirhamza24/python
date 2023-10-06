# remove item from list
# the remove() method remove the specific item using list data.
newList = ["Juwel", "Ratul", "Rabbi", "Rashed", "Imran", 497]
print(newList)
newList.remove("Rabbi")  # newList.remove(497)
print(newList)

# the pop() method remove the specific item using index.
# pop() method er moddhe jodi kono index na dei tahole last index er value ta remove korbe.
newList.pop(3)
print(newList)

# the del keyword also remove the specific index. ekhaneu j index er value ta remove korte chai seta bole dibo
del newList[1]
print(newList)


# the clear() method empties the list. eta list er all data k remove kore dibe
newList.clear()
print(newList)