# **什麼是繼承 inheritance？**

# A：繼承，就如同字面上的意思：父親繼承了爺爺的東西，兒子繼承父親的東西...不斷繼承下去

# 繼承表示可以用既有的類別去建立一個新的類別，並加入一些新的東西或修改新的類別，當使用繼承時，新的類別會自動使用舊的類別內所有的程式碼

# 範例：
# son 繼承了 father
class father():         # fatehr 類別
    def __init__(self):
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1

class son(father):          # son 類別繼承了 fatehr 類別裡所有的方法
    def language(self):     # son 類別具有 language 的方法
        print('chinese')    # 從 father 繼承了五官，然後自己學會講中文

oxxo = son()                # 設定 oxxo 為 son()
print(oxxo.eye)             # 印出 2
oxxo.language()             # 印出 chinese

# *****************************************************************************************************************

# 繼承 覆寫
# 如果子類類別裡某個方法的名稱和父類別相同，則會完全複寫父類別的方法

# 範例：
# 下面的程式碼，son 類別使用了 init 的方法，就覆寫了原本 fatehr 的 init 方法，導致讀取 oxxo.ear 時發生錯誤 ( 因為 son 的方法裡不存在 ear 的屬性 )
class father():
    def __init__(self):
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1

class son(father):
    def __init__(self):   # 使用了 __init 的方法
        self.eye = 100

oxxo = son()
print(oxxo.eye)    # 100
print(oxxo.ear)    # 發生錯誤  'son' object has no attribute 'ear'

# *****************************************************************************************************************

# ***`super()`***

# 如果***不想要覆寫父類別的方法，又想要使用父類別的方法***，就可以使用「***`super()`***」來實現
class father():
    def __init__(self):
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1

class son(father):
    def __init__(self):
        super().__init__()   # 使用 super() 繼承 father __init__ 裡 "所有屬性"
        self.eye = 100       # 如果屬性相同，則覆寫屬性

oxxo = son()
print(oxxo.eye)              # 100
print(oxxo.ear)              # 2

# *****************************************************************************************************************

# # 多重繼承

# 多重繼承：
# 繼承不僅能進行單一繼承，也可以進行多重繼承
class father():          # father 類別
    def __init__(self):  # father 的方法
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1

class mother():          # mother 類別
    def language(self):  # mother 的方法
        print('english')
    def skill(self):
        print('painting')

class son(father, mother):    # 繼承 father 和 mother
    def play(self):           # son 自己的方法
        print('ball')

oxxo = son()
print(oxxo.eye)        # 2
oxxo.skill()           # painting
oxxo.play()            # ball

# *****************************************************************************************************************

# 多層繼承
# 如同***父親繼承了爺爺的東西，兒子繼承父親的東西***

# 多層繼承同樣存在覆寫方法的原則，如果遇到同名的方法就會覆寫，除非使用 super() 的方法處理

# 下方的例子裡， father 繼承了 grandpa 的五官，son 又繼承了 father 的方法，最後 son 就擁有 father 和 grandpa 所有的方法。
class grandpa():
    def __init__(self):
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1

class father(grandpa):
    def language(self):
        print('english')
    def skill(self):
        print('painting')

class son(father):
    def play(self):
        print('ball')

oxxo = son()
print(oxxo.eye)    # 2
oxxo.skill()       # painting
oxxo.play()        # ball

# *****************************************************************************************************************

# # **私有方法 ( 雙底線 )**
# 在實作一個類別的過程裡，可能會遇到有些方法是該類別內部使用，不想讓繼承該類別的子類別可以使用的
# 這時就需要建立「私有方法」，私有方法可以使用「**`雙底線 + 名稱`**」來建立
# **私有方法建立後，不論是從外部讀取或是子類別的繼承，都無法使用該方法，只有在該類別裡的其他方法才能調用**。

# 可以藉由”getMoney”，得知”self.__money()”的資料，但是無法直接呼叫”__money”功能
class grandpa():
    def __init__(self):
        self.mouth = 1
    def __money(self):     # 建立一個私有方法 __money
        print('$1000')
    def getMoney(self):    # 建立一個 getMoney 的方法，執行私有方法 __money
        self.__money()

class father(grandpa):
    def skill(self):
        print('painting')

class son(father):
    def play(self):
        print('ball')

oxxo = son()
oxxo.getMoney()         # $1000
oxxo.__money()          # 發生錯誤  'son' object has no attribute '_money'