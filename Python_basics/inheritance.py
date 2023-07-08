class Mammal:
    def walk(self):
        print("walk")

    def talk(self):
        print(f"{self.voice} is {self.age}")

    def __init__(self, voice, age):
        self.voice = voice
        self.age = age


class Dog(Mammal):

    def __init__(self, age):
        super().__init__("bark", age)


class Cat(Mammal):
    def __init__(self, age):
        super().__init__("Meow", age)


dog1 = Dog(56)
dog1.talk()
mammal = Mammal("hello", 35)
