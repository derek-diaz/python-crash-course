class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + ' eats')

    def sleep(self):
        print(self.name + ' sleeps')


dog = Animal('Spots')

dog.eat()

dog.sleep()