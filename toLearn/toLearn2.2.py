#2.2 Inheritance
class Human:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print(f"hello my name is {self.name}")

class Player(Human):
    def __init__(self, name, xp):
        # self.name = name
        self.xp = xp
    # def say_hello(self):
    #     print(f"hello my name is {self.name}")

class Fan(Human):
    def __init__(self, name, fav_team)
        # self.name = name
        self.fav_team = fav_team
    # def say_hello(self):
    #     print(f"hello my name is {self.name}")

manju_player = Player("manju", 10)
manju_player.say_hello()
milk_player = Fan("milk", "dontknow")
milk_player.say_hello()

# Inheritance
# class 클래스명(부모 클래스):
# : class끼리의 inheritance(상속)은 Java, TypeScript에서는 extends로 작성했지만 
# python에서는 클래스명 옆 () 안에 부모클래스 이름을 적는다.
