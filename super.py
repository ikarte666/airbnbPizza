class Dog:
    def __init__(self):
        print("hooting")

    def pee(self):
        print("I will pee")


class Puppy(Dog):
    def __init__(self):
        print("im tiny")
        super().__init__()
