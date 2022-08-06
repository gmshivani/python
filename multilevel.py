class Animal:
    def speak(self):
        print("Animal Speaking")
    #child class Dog inherits the base class Animal


class Dog(Animal):
    def bark(self):
        print("dog barking")


class DogChild(Dog):
    def eat(self):
        print("eating bread")


d = DogChild()
d.speak()
d.bark()
d.eat()