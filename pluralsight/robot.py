class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print(f'My name is {self.name}')

    def walk(self, x):
        self.position[0] += x
        print('New Position:', self.position)

    def eat(self):
        print('I am hungry')

class Robot_Cat(Robot):

    def make_noise(self): 
        print('Meawooo')

    def eat(self):
        super().eat()
        print('I want a rat')

my_robot = Robot_Cat('Puss')
my_robot.make_noise()
my_robot.walk(5)
my_robot.eat()