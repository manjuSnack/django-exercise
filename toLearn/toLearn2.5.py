#2.5 dir
class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        print(super().__str__()) # <__main__.Dog object at 0x~>
        return f"Dog:{self.name}"
    def __getattribute__(self, name):
        print("they want to get {name}")
        return "🧃"

jia = Dog("jia")
print(jia)
print(jia.name) # "they want to get {name}" "🧃"
print(dir(jia)) 

paul = Dog("paul")
print(paul)

# dir()
# : Directory를 의미하며 Class의 property와 method를 보여준다.
# __init__, __str__, __dict__, __delattr__ 등 사용할 수 있는 method를 전부 보여준다.

# __str__()
# : 상속받은 class에서 print()를 사용 시 Class가 출력되는데, 
# '<__main__.~ object at 0x~>'와 같은 출력형식을 바꾸어 줄 수 있다.

# __getattribute__()
# : self.name과 같은 property(혹 attribute)에 접근하는 경우 수행하는 method
