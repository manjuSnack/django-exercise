# Python
# Class 구현 시 아래와 같다.
class Player:{
    def __init__(self, name, health, skill):
        self.name = name
        self.health = health
        self.skill = skill
        self.xp = 0
    def sayHello(self):
        return f'Hi, my name is {self.name} and my skill is {self.skill}'
    def takeHit(self):
        self.health = self.health - 5
}

bill = Player("Bill Gates", 85, "Programmer");
elon = Player("Elon Musk", 90, "Legend");
warren = Player("Warren Buffett", 100, "Investor");
print(warren.health);
print(warren.takeHit());

# __init__(): = Method
# self : Java, JavaScript에서의 this와 같다. Class 내 인스턴스 변수와 인스턴스 메서드를 참조한다.

class Human:{
    def __init__(self, name):
        self.name = name
        self.arms = 2
        self.legs = 2
}

class Baby:{
    def __init__(self, name):
        # self.name = name
        # self.arms = 2
        # self.legs = 2
        
        self.cute = True;
    def cry(self)
        return f'waa waa'
}

class Teenager:{
    def __init__(self, name):
        # self.name=name
        # self.arms = 2
        # self.legs = 2
        self.emotional = True;
    def curse(self)
        return f'#$18%@&!'
}


