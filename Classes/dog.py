from Animal import Animal

class Dog(Animal):
    def __init__(self, name, age, breed='husky'):
        super().__init__(name, age, breed)

    # Переопределение метода __str__
    def __str__(self):
        return f'Собака {self.name} ({self.breed}) — {self.age} лет'

    # Переопределение метода speak
    def speak(self, sound='Гав'):
        print(f'{self.name} говорит: {sound}')

    def defend(self):
        print(f'{self.name} защищается!')


dog = Dog(name='Rex', age=5, breed='husky')
print(dog)
dog.speak()
dog.speak('Рррр')
dog.defend()
