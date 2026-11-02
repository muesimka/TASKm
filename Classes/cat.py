from Animal import Animal

class Cat(Animal):
    def __init__(self, name, age, breed='cat'):
        super().__init__(name, age, breed)

    # Переопределение метода __str__
    def __str__(self):
        return f'Кошка {self.name} ({self.breed}) — {self.age} лет'

    # Переопределение метода speak
    def speak(self, sound='Мяу'):
        print(f'{self.name} говорит: {sound}')


cat1 = Cat(name='Marusya', age=10)
cat2 = Cat(name='John', age=11)

print(cat1)
print(cat2)
cat1.speak()
cat2.speak('Мррр')
