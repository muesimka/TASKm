 class Animal:
     def __init__(self, name=None,, age=None, breed=''):
         self.name = name
         self.age = age
         self.breed = breed


    def __str__(self):
         return f'This {self.breed} - {self.name} is {self.age} years old'


    def speak(self, sound):
         print(sound)
