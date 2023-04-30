#2.3 super()
class Human:
    def __init__(self, name):
        print("human initialized")
        self.name = name
    def say_hello(self):
        print(f"hello my name is {self.name}")

class Player(Human):
    def __init__(self, name, xp):
        # super().__init__(name) # super가 없는 경우 부모 클래스에는 접근할 수 없다.
        self.xp = xp

class Fan(Human):
    def __init__(self, name, fav_team)
        super().__init__(name)
        self.fav_team = fav_team

manju = Fan("manju", "yellow")
manju.say_hello()

# super
# super().__init__(parameter) : super()를 작성함으로써 부모 클래스의 접근할 수 있다. 이때 __init__은 부모 클래스의 __init__이다.
# Java, TypeScript와는 다르게 'super().__init__()'이 없는 경우에는 부모 클래스에 접근할 수 없다.