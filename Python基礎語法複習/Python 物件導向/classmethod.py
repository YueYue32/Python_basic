# classmethod
# Class method 類方法：不帶實例，帶有 class 為參數的方法

# https://ji3g4zo6qi6.medium.com/python-tips-5d36df9f6ad5
# https://www.learncodewithmike.com/2020/01/python-method.html

# *********************************************************************************************************

# ClassMethods 使用方法：

# 在 def 函式上加上 @classmethod

# 必須傳入 class 本身參數，通常大家都會命名為 cls

# 如果要引入 class 其他函式，可以使用 cls().XXX(Y)

# ClassMethods 使用時機：

# 不在需要將 class 實例後才能使用函式，直接像以下範例呼叫 People_ClassMethods.work(5) 即可

# 不同於 StaticMethods，因為多引入了 class 本身參數為 cls，可以利用 cls 來 access 其他 class 內的函式

class People_ClassMethods:
    def __init__(self):
        pass

    def sleep(self, sleep_hour):
        print('Sleeping hours :', sleep_hour)

    @classmethod
    def work(cls, work_hour):
        print('Working hours :', work_hour)
        cls().sleep(6)  # 利用cls呼叫其他功能


People_ClassMethods.work(5)  # 可直接使用class，不須經過實例化

# *********************************************************************************************************

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person = Person('Adam', 19)
person.display()

person1 = Person.fromBirthYear('John',  1985)
person1.display()


#Output
# Adam's age is: 19
# John's age is: 31

# *********************************************************************************************************

# 類別方法(Class Method)的cls參數指向類別(Class)，所以類別方法(Class Method)僅能改變類別的狀態，而無法改變物件(Object)的狀態
# 因為它沒有self參數可以存取物件的屬性(Attribute)及方法(Method)。
# 汽車類別
class Cars:
    door = 4  # 類別屬性
    # 類別方法(Class Method)
    @classmethod
    def open_door(cls):
        print(f"{cls} has {cls.door} doors.")
mazda = Cars()
mazda.open_door()  #透過物件呼叫
Cars.open_door()  #透過類別呼叫

# *********************************************************************************************************

# 以這個範例來說，不一定要透過類別方法(Class Method)來建立物件(Object)，可以單純透過建構子(Constructor)即可
#
# 主要是要表達當建立物件(Object)的邏輯較複雜時，透過類別方法(Class Method)可以將邏輯封裝起來，來源端只要依需求呼叫相應的類別方法(Class Method)來建立物件(Object)即可
#
# 就像範例中，想要跑車則呼叫跑車類別方法(Class Method)來建立跑車，至於物件(Object)的初始化過程(建造跑車的過程)封裝在類別方法中(Class Method)
# 它會幫我們完成並回傳，就像建立物件(Object)的工廠一樣，所以類別方法(Class Method)也被稱為工廠方法(Factory Method)，讓程式碼簡潔且易於維護

# 汽車類別
class Cars:
    # 建構式
    def __init__(self, seat, color):
        self.seat = seat
        self.color = color

    # 廂型車
    @classmethod
    def van(cls):
        return cls(6, "black")

    # 跑車
    @classmethod
    def sports_car(cls):
        return cls(4, "yellow")

van = Cars.van()
sports_car = Cars.sports_car()