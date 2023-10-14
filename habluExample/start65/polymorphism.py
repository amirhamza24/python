class vehicle:
    def __init__(self, model, brand, component):
        self.model = model
        self.brand = brand
        self.component = component

class plane(vehicle):
    pass
class car(vehicle):
    pass

class bike(vehicle):
    pass

p1 = plane("Hablu428", "hablu", "All component")
c1 = car("BMW", "E223", "Main Component")
b1 = bike("R15", "V3", "component")

print(p1.model, p1.brand, p1.component)
print(c1.model, c1.brand, c1.component)
print(b1.model, b1.brand, b1.component)