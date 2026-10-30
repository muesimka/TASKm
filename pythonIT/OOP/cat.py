from Animal import Animal

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name,age)

cat1 = Cat(name="Marusya", age=10)
cat2 = Cat(name="John", age=11)
print(cat1.__str__(), cat2.__str__())
cat1.speak("Meow")
cat2.speak("Mrr")
