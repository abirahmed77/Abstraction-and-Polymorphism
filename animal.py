class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        print(f"I am a Cat. My name is {self.name}. I am {self.age} years old.")
        
    def makesound(self):
        print("Meow")
        
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        print(f"I am a Dog. My name is {self.name}. I am {self.age} years old.")
        
    def makesound(self):
        print("Gheu Gheu")
        
cat1 = Cat("Kitty", 3)
dog1 = Dog("Puppy", 4)

for animal in (cat1, dog1):
    animal.makesound()
    animal.info()
    animal.makesound()
    print()