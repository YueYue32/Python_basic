# https://steam.oxxostudio.tw/category/python/basic/closure.html
# https://medium.com/@zhoumax/python-%E9%96%89%E5%8C%85-closure-c98c24e52770
# https://ithelp.ithome.com.tw/articles/10311658

# 在內部函數中引用了外部函數的變量，並且外部函數已經返回了內部函數。
#
# 這種情況下，內部函數將保留對外部函數變量的引用，即使外部函數已經完成執行。這種引用關係就形成了閉包
#
# 範例：
#
# 1. 閉包部分是 "plus_y”
# 2. add_5 = plus_x(5)， plus_x(5) 是呼叫外層的"plus_x"
# 3. 但是因為"plus_x"內部還有一個功能 “plus_y”，所以"add_5" 這時是指向"plus_y" 這個功能
# 4. 因為"add_5" 這時是指向"plus_y" 這個功能，所以 print(add_5)時，才會顯示出這是一個 function
# 5. 所以如果要呼叫內部閉包功能"plus_y"，呼叫"add_5" 這個功能，再給他需要的參數
def plus_x(x):
    print("in plus_x")

    def plus_y(y):
        print("in plus_y")

        return x + y
    return plus_y


add_5 = plus_x(5)

# print(add_5)  # <function plus_x.<locals>.plus_y at 0x000001B142A20430>

print(add_5(2))  # 7

