# 2.4 OOP with Python Recap
class Dog:
    def woof(self):
        print("woof woof")

class Beagle(Dog):
    def jump(self):
        print("jump")
    def woof(self):
        super().woof() # super()로 Dog class에 woof()를 불러올 수 있다.
        print("woof woof woof") # overriding

beagle = Beagle()
beagle.woof()


# oop Recap

