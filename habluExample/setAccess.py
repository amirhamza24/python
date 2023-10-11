setAccess = { 15,2,35,4,52,6 }
for i in setAccess:
    print(i)

print(15 in setAccess)  # eta diye dekhchi list er moddhe 15 ache kina. thakle "true" dibe na thakle "false" dekhabe...


# add set
addSet = { "Apple", "Mango", "Banana", "Orange" }
addSet.add("Cherry")  #adding new item in the set using add() method
print(addSet)

# set update()
set1 = { "Apple", "Mango", "Banana", "Orange" }
set2 = { 1,2,3}

set1.update(set2)  # ekhane set2 er all data set1 er moddhe chole jabe and eksathe set1 er moddhei sob gula add hoye jabe...
print(set1)
