class Robot_Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof!"

    def fetch(self, item):
        return f"{self.name} fetched the {item}!"
    
my_dog = Robot_Dog("RoboBuddy")
print(my_dog.bark())
print(my_dog.fetch("ball"))
print(my_dog.fetch("stick"))