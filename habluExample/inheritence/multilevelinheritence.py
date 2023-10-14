class parentClass1:
    car = "BMW"
    tk = "100 Crore"
    home = "10 Home"

class parentClass2(parentClass1):
    phone = "Samsung"
    ac = "Walton"
    microphone = "Fifine"

class parentClass3(parentClass2):
    webcam = "Iphone"
    laptop = "hp"
    camera = "Fifine"

class childClass(parentClass3):
    brokenHome: ""
    brokenPhone: ""

k = childClass()
print(k.car)
print(k.home)

print(k.ac)
print(k.laptop)