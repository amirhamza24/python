list = [1,2,3,4, "Rakib", "Sakib", "Sojib"]

# for i in list:
#     print(i)

x = iter(list)

# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())  # egula ekta ekta kore value dekhabe. mane protibar call korar jonno ekta kore value dekhabe
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

print(next(x))
print(next(x))   # etau same kaaj.. protibar print korar jonno protibar print korte hobe...
print(next(x))
