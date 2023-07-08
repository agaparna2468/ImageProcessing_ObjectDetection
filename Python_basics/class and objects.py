class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} can talk")


ayush = Person("Ayush")
ayush.talk()
