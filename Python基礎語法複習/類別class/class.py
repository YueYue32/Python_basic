# https://steam.oxxostudio.tw/category/python/basic/class.html

# ********************************************************************************************************

# 類似建立一個函式，差別在於函式使用 def 開頭，而類別使用 class 開頭
# 建立空類別
class human():
    pass        # 使用 pass 可以建立一個空類別

# ********************************************************************************************************

# __init__
# 建立類別的預設方法「__init__」( 注意前後是兩條底線 )，將預設的屬性加入類別裡

# def __init__(self)：
# 預設帶有一個 self 參數，代表透過類別建立的物件本體
# 內容使用「.屬性」就能將指定的屬性加入類別中。

# __init__ ：
# 可以不用定義，但如果需要有一些預設的屬性，就可以定義在裡面

class human():
    def __init__(self):  # 建立預設屬性的寫法
        self.eye = 2       # 兩個眼睛
        self.ear = 2       # 兩個耳朵
        self.nose = 1      # 一個鼻子
        self.mouth = 1     # 一張嘴巴

# ********************************************************************************************************

# 除了預設的屬性，也可以自訂屬性
class human():
    def __init__(self):
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1

    def say(self, msg):      # 定義 say
        print(msg)

    def play(self, thing):   # 定義 play
        print(thing)


oxxo = human()    # 製作一個名為 oxxo 的物件
oxxo.say('hello')          # hello
oxxo.play('baseball')      # baseball


# 屬性除了可以定義在類別裡，也可以從外部定義
class human():
    def __init__(self):
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1
    def say(self, msg):
        print(msg)
    def play(self, thing):
        print(thing)

human.hand = 2    # 定義 hand 屬性
human.leg = 2     # 定義 leg 屬性

oxxo = human()
print(oxxo.hand)  # 2
print(oxxo.leg)   # 2

# ********************************************************************************************************

# 使用 self 可以讀取到這個物件的所有屬性
class human():
    def __init__(self):
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1

    def say(self, msg):
        print(f'{self.name} say: {msg}')   # 使用 self.name 取得 name 屬性的值

    def play(self, thing):
        print(thing)


oxxo = human()
oxxo.name = 'oxxo'   # 設定 name 屬性
oxxo.say('hello')    # oxxo say: hello

# ********************************************************************************************************

# 不同物件套用同一個功能
class human():
    def __init__(self):
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1
    def say(self, msg):
        print(f'{self.name} say: {msg}')
    def play(self, thing):
        print(thing)

oxxo = human()        # 定義 oxxo
oxxo.name = 'oxxo'    # oxxo 的名字叫做 oxxo
oxxo.age = 18         # oxxo 的 age 為 18

gkpen = human()       # 定義 gkpen
gkpen.name = 'gkpen'  # gkpen 的名字叫做 gkpen
gkpen.weight = 70     # gkpen 的 weight 為 70


oxxo.say('hello')    # oxxo say: hello
print(oxxo.age)      # 18


gkpen.say('song')    # gkpen say: song
print(gkpen.weight)  # 70

# ********************************************************************************************************

# 設定參數
# 在建立類別時，預先設定好一些參數，接著透過類別建立物件時，在做動態的調整
class human():
    def __init__(self, age, weight):    # 新增 age 和 weight 參數
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1
        self.age = age             # 讀取參數，變成屬性
        self.weight = weight       # 讀取參數，變成屬性

    def say(self, msg):
        print(f'{self.name} say: {msg}')

    def play(self, thing):
        print(thing)

oxxo = human(18, 68)            # 建立物件時，設定參數數值
gkpen = human(15, 70)           # 建立物件時，設定參數數值
print(oxxo.age, oxxo.weight)    # 18, 68
print(gkpen.age, gkpen.weight)  # 15, 70

# ********************************************************************************************************

# 覆寫屬性
# 從外部定義了和類別屬性名稱相同的屬性，就會覆寫內部屬性
class human():
    def __init__(self):
        self.eye = 2
        self.ear = 2
        self.nose = 1
        self.mouth = 1

    def say(self, msg):
        print(f'{self.name} say: {msg}')

    def play(self, thing):
        print(thing)


oxxo = human()
oxxo.eye = 5  # 覆寫 eye 屬性
print(oxxo.eye)  # 5

# ********************************************************************************************************

# @property 唯讀屬性
# 如果在類別裡有些屬性不希望被外部更動，就能夠使用 @property 的裝飾器，將該屬性設為唯讀屬性
class a:
    def a(self):
        return 'aaaaa'

    @property
    def b(self):
        return 'bbbbb'

oxxo = a()


oxxo.a = '12345'
print(oxxo.a)   # 12345


oxxo.b = '12345'
print(oxxo.b)   # 發生錯誤  can't set attribute