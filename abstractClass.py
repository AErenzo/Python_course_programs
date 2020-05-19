from abc import ABC, abstractmethod

class Animal(ABC):
    
    __name = 0
    
    def __init__(self, name):
        self.setName(name)

    @abstractmethod
    def makeNoise(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    def move(self):
        print('I can move')

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def __str__(self):
        return 'Name: {}'.format(self.getName())

        


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)
        #self.__name = name

    def makeNoise(self):
        print('Woof')
        #print('Hello my name is', self.__name)

    def eat(self):
        print('Give me treats')


class Cat(Animal):
 

    def __init__(self, name):
        super().__init__(name)

    def makeNoise(self):
        print('Meow - fuck off')
        #print('Hello my name is', super(name).__init__())

    def eat(self):
        print('I eat shit')


class Hippo(Animal):

    def __init__(self, name):
        super().__init__(name)

    def makeNoise(self):
        print('Boo')
        #print('Hello my name is', getName())

    def eat(self):
        print('Give me some sugar')


D1 = Dog('Betty')

print(D1)
D1.makeNoise()
D1.eat()
D1.move()
print(D1.getName())

C1 = Cat('Cunt')

print(C1)
C1.makeNoise()
C1.eat()
C1.move()

H1 = Hippo('Clive')

print(H1)
H1.makeNoise()
H1.eat()
H1.move()
    
    
