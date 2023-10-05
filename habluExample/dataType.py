# int type data
hablu = 420
print(hablu)
print(type(hablu))


# floating type data
gablu = 40.2
print(type(gablu))


# complex type er datar sathe always shudhu 'j' ta dite hobe. Onno kono kichuna just j
jablu = 2385j
print(jablu)
print(type(jablu))


# Boolean type data
habluBool = True
print(habluBool)
print(type(habluBool))


# String formatting
num1 = 50
num2 = 20
userName = "Ridoy"
roll = "24"

print(f"The Result is: {num1 + num2}")
print(f"My name is {userName}")
print(f"My name is: {userName} & My Roll is: {roll}")


# binary type data (byte) .. byte data type is immutable, that means unchangeable
habluList = [1, 2, 3, 45, 23, 75, 169, 65]

b = bytes(habluList)
print(type(b))

# binary type data (byteArray) .. bytearray is mutable. It is changeable
habluList1 = [2, 4, 7, 45, 21, 85, 141]

b1 = bytearray(habluList1)
b1[1] = 100

print(type(b1))
print(b1[1])


# none data type
x = None
print(type(x))


# sequence type data (list) list data type mutuable. So we can change or update list data type value.
li = ["eshan", 'shawon', "badhon", "hasan", "rakib"]
li[0] = "ashik"
print(type(li))
print(li)

# sequence type data (tuple). this data type is immutable. we cannot change or update this value.
tup = (4, 63, 41, 23, 19)
print(tup)
print(type(tup))

# sequence type data (range).
ran = range(6)

for i in ran:
    print(i)
print(type(ran))
