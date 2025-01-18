class Human:
    age = 25
    height = 160
    name = "q"
    def __init__(self, age, height, name):
        self.age = age
        self.height = height
        self.name = name

    def say_hello(self):
        print("Hi!")
    def say_bye(self):
        print("Bye!")

bober = Human(25, 210, "bobr")
print(bober.name)
print(bober.age)
bober.say_bye()