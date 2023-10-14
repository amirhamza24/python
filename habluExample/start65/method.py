class className:
    def instanceMethod(self):
        print("This is instance method")

    @classmethod
    def classMethod(cls):
        print("This is class method")

    @staticmethod
    def staticMethod():
        print("This is static method")

instance = className()

instance.instanceMethod()
instance.classMethod()
instance.staticMethod()


