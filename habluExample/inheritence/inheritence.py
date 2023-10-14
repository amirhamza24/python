class parentClass:
    car = "BMW"
    tk = "100 Crore"
    home = "10 Home"

class childClass(parentClass):
    brokenHome: ""
    brokenPhone: ""

k = childClass()
print(k.car)
print(k.home)