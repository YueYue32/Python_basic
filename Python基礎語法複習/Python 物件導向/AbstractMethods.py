# AbstractMethods 抽象方法
# AbstractMethods 使用時機：
#
# 抽象類 的特點是不能實例化，只能被子類繼承
#
# 任何繼承抽象類，都必須實現 包含上層內的“功能” ，否則會拋出異常
#
# 例如像是 class Max(Employee) 中，只定義了 def sleep(self)，沒有定義 “work” 方法，所以再引用時會出現 Can’t instantiate abstractclass Max with abstract methods work 的錯誤。


# 白話文：最上層的class，裡面有哪些功能，底下繼承的class就必須包含哪些功能，缺一不可
#
# 下面範例，以白話文來說，就是上層的class Employee，內部含有一個”work”功能，但是繼承class Employee的class Max(Employee)，沒有包含”work”功能，所以呼叫時會報錯
#
# 在最上層的class裡面，功能的前面加入@abc.abstractmethod
import abc


# Python 3.4+

class Employee(abc.ABC):
    @abc.abstractmethod
    def work(self):
        return NotImplemented


class Andy(Employee):
    def work(self):
        print('work')


class Max(Employee):
    def sleep(self):
        print('sleep')


Andy().work()
>> > work

Max().sleep()

# >>> Traceback (most recent call last):
#   File "/Users/max/Desktop/python_learning/methods.py", line 77, in <module>
#     Max().sleep()
# TypeError: Can't instantiate abstractclass Max with abstract methods work

# *****************************************************************************************************************

# 簡易寫法：
#
# 在前面加入from abc import ABC, abstractmethod
# @abc.abstractmethod 改成  @abstractmethod

from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def work(self):
        return NotImplemented


class Andy(Employee):
    def work(self):
        print('work')


class Max(Employee):
    def sleep(self):
        print('sleep')


Andy().work()
>> > work

Max().sleep()

# >>> Traceback (most recent call last):
#   File "/Users/max/Desktop/python_learning/methods.py", line 77, in <module>
#     Max().sleep()
# TypeError: Can't instantiate abstractclass Max with abstract methods work