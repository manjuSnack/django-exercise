#2.1 __init__
# TypeScript → python
class Player:
    def __init__(self, name, xp):
        # self.name = "manju"
        self.name = name
        self.xp = xp
    def say_hello(self):
        print(f"hello my name is {self.name}")

# manju = Player() 
# print(manju.name)

manju = Player("manjuSnack", 1000)
print(manju.name, manju.xp)

manju.say_hello()

# TypeScript → python
# def __init__(self):
# : __init__은 JavaScript에서의 constructor와 같은 역할이며 self를 인자로 하여 해당 class의 instance를 가리킨다.
# : __init__은 initailize constructor의 약자이다.
# : __init__은 property를 정의하고자 할 때에만 사용한다.

# self : self는 Java, JavaScript에서의 this와 같은 역할을 한다. 
# method() 처럼 빈 parameter인 경우 Error가 발생하므로 self로 작성해야 한다.

# 변수 = 클래스명()
# : Python에서는 new 연산자를 쓰지 않고 Instance를 생성한다.

# Python은 private, public, type을 지원하지 않아 간결하게 작성할 수 있다.
