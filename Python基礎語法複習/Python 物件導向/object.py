# Python 物件導向.

# 繼承 (inheritance)
class Employee:
    def __init__(self):
        self.cut_tree = 3


class Andy(Employee):  # Andy 繼承 Employee物件
    def __init__(self, get_gold):
        super().__init__()  # super() 是呼叫父類別的語法，所以繼承了父親的能力
        self.get_gold = get_gold

    def getDetials(self):
        print('tree:', self.cut_tree)  # 繼承後即可使用父親的能力
        print('gold:', self.get_gold)


if __name__ == "__main__":
    andy = Andy(1)
    andy.getDetials()

# ***********************************************************************************

# 封裝 (encapsulation)
# 隱藏程式的功能細節，只保留下接口，使程式容易模組化
#
# 白話文：看的到包裝，但是看不到包裝內的東西
#
# 例如：像是手機，從開機、打電話到上網我們不知道背後具體實現的細節，但只需要按下按鈕就可以完成，這功能就是封裝
#
# ================================================================
#
# 以下範例 work() 就是封裝的表現，可以讓外部使用者不需考慮內部實作而直接呼叫使用。
#
# 若是有不想被呼叫的變數，直接在前面加上 __ ，像是 __sleep即可以成為私有變數
#
# 注意：
#
# 是加2條底線__，不是1條
#
# 只加入一條底線，不會影響到功能，但是是警告user最好不要使用
#
# 如果使用者呼叫 __sleep 時則會噴 object has no attribute 的錯誤。
class Employee:
    def __init__(self):
        self.cut_tree = 3

    def work(self):
        print(‘Working’)

        def __sleep(self):
            print(‘Sleeping’)


            if __name__ == “__main__”:
                Andy = Employee()

                andy.work()
                >> > Working

                andy.__sleep()
# >>> AttributeError: ‘Employee’ object hasno attribute ‘__sleep’


# ***********************************************************************************

# 多型 (polymorphism)
# 呼叫同名的方法時，會得到不同的結果
#
# 如下範例 Employee、Andy 和 Joy 類別都同時擁有 work 的方法
#
# 但呼叫 w.work()、w1.work()、w2.work() 時卻有各自的表現形態。
#
# Python 會根據呼叫的類別來決定要執行哪個方法實作，這就是多型的意思。
class Employee:
    def work(self):
        print(‘Employee
        work’)

        class Andy(Employee):
            def work(self):
                print(‘Andy
                work’)

                class Joy(Employee):
                    def work(self):
                        print(‘Joy
                        work’)


                        w = Employee()
                        w1 = Andy()
                        w2 = Joy()

                        w.work()
                        w1.work()
                        w2.work()

# >>> Employee work
# >>> Andy work
# >>> Joy work