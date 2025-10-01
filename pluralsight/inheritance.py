class MyClass(object):
    common = 10

    def __init__(self):
        pass

    def add(self, number: int) -> int:
        print(self.common + number)
        print(MyClass.common + number)
    

class MySubClass(MyClass):
    
    def __init__(self, arg1: int):
        self.var1 = arg1
        print(arg1)

myinstance = MyClass()
myinstance.common = 20
myinstance.add(20)
print('--------------------')
mySubInstance = MySubClass(100)
mySubInstance.common = 40
mySubInstance.add(20)