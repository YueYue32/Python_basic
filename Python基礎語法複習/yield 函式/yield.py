# https://ithelp.ithome.com.tw/articles/10258195
# https://chriskang028.medium.com/python-%E8%A3%A1%E7%9A%84-yield-%E8%AE%93%E4%BD%A0%E7%B0%A1%E5%96%AE-%E5%BF%AB%E9%80%9F%E7%9E%AD%E8%A7%A3-yield-%E7%9A%84%E6%A6%82%E5%BF%B5-f660521f3aa7

# 加入yeild 函式的目的
# 為了節省”記憶體”
# 如果要儲存的資料有上百萬筆，記憶體可能會承受不了，程式就炸了。

# *******************************************************************************************************************

# 加入yield 函式
# 函數加入yield後不再是一般的函數，而被視作為生成器(generator)
# 呼叫函數後，回傳的並非數值，而是函數的生成器物件。

def yield_test(n):
    print("start n =", n)
    for i in range(n):
        yield i * i
        print("i =", i)

    print("end")


if __name__ == "__main__":
    tests = yield_test(5)

    for test in tests:
        print("test =", test)
        print("--------")

# *******************************************************************************************************************

# 也可以用next()函式 呼叫
def yield_test(n):
    print("start n =", n)
    for i in range(n):
        yield i*i
        print("i =", i)

    print("end")


if __name__ == "__main__":

    tests = yield_test(5)

    print("tests = ", next(tests))
    print("====================")

    print("tests = ", next(tests))
    print("====================")

    print("tests = ", next(tests))
    print("====================")

    print("tests = ", next(tests))
    print("====================")