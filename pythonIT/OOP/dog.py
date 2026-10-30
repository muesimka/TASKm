from Animal import Animal

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)

    def defend(self):
        print("Dog is defending")

dog = Dog(name='Dog', age=20, breed="husky")
print(dog.__str__())