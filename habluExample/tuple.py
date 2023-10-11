# tuple access
tupleList = ( 1, 32, 45, 3, 8 )
print(tupleList[-2])

tupleRange = ( 1, 2, 4, "Banana", "Apple", "Orange", "Mango", "kiwi" )

print(tupleRange[2:5])


# tuple update
thisList = ('Rakib', 'Sakib', 'Sojib', 'Rohim', 'Korim')

print(type(thisList))

a = list(thisList)
a.append("Sahin")

updateValue = tuple(a)

print(type(a))
print(a)
print(thisList)
print(updateValue)
print(type(updateValue))


# unpack tuple
unpackList = ("Apple", "Mango", "Banana", "Orange")

(a, b, *c, ) = unpackList  # first a "a" r "b" value niye baki sob gulo value c er moddhe jabe..
print(a)


# tuple loop
tupleLoop = ("Apple", "Mango", "Banana", "Orange", "kiwi", "Cherry")

for i in tupleLoop:
    print(i)  # ekhane shudhu list er value gulo dekhabe

for x in range(len(tupleLoop)):
    print(x)  # ekhane list er index er number dekhabe
    print(tupleLoop[x])  # evabeu list er value dekhano jay range use kore..


# tuple join
tupleJoin = (1, 2, 3, "Apple", "Mango", "Banana")
print(tupleJoin * 2) # output: (1, 2, 3, 'Apple', 'Mango', 'Banana', 1, 2, 3, 'Apple', 'Mango', 'Banana')


# tuple count
tupleCount = (1,2,3,4,5,2,14,5,2,2,1)
print(tupleCount.count(2))  #output: 4

# tuple index
tupleIndex = ( "Apple", "Mango", "Banana", "Orange" )
print(tupleIndex.index("Banana"))  # output: 2