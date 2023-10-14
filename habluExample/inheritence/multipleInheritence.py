class parentClass1:
    car = "BMW"
    tk = "100 Crore"
    home = "10 Home"

class parentClass2:
    phone = "Samsung"
    ac = "Walton"
    microphone = "Fifine"

class parentClass3:
    webcam = "Iphone"
    laptop = "hp"
    camera = "Fifine"

class childClass(parentClass1, parentClass2, parentClass3):
    brokenHome: ""
    brokenPhone: ""

k = childClass()
print(k.car)
print(k.home)

print(k.ac)
print(k.laptop)