# using function inside class
class parentClass:
    def rakibFamily(self, name, age):
        print(f"My name is: {name} & My age is: {age}")

a = parentClass()

a.rakibFamily("Sakib", 15)
a.rakibFamily("Sojib", 22)
a.rakibFamily("Nakib", 25)



# parameterized constructor
class parentInfo:
    def __init__(self, name, number):
        print(f"My name is: {name}, & My number is: {number}")

x = parentInfo("Roni", "019238294")