# 語法糖 (syntax suger)
# 其他替代 “包裝函式” 的方法 — 語法糖 (syntax suger)
#
# 加入語法糖 (syntax suger)後，改寫成以下
from functools import wraps
import time


def timer(func):
    def wrap(sleep_time):
        t_start = time.time()
        func(sleep_time)
        t_end = time.time()
        t_count = t_end - t_start
        print('[花費時間]', t_count)

    return wrap


@timer
def dosomething(sleep_time):
    print('do some thing')
    time.sleep(sleep_time)


dosomething(3)

# ****************************************************************************************************

# 語法糖的邏輯概念：
# @外層程式
# def 主程式():

# 加入語法糖之後，就能直接調用、呼叫語法糖之下的主程式


# ****************************************************************************************************

# 加入語法糖的副作用：函式名稱 改變
# 裝飾詞在被 wrap 包一層後，其 name 屬性就會被修改成 wrap
from functools import wraps
import time


def timer(func):
    def wrap():
        t_start = time.time()
        func()
        t_end = time.time()
        t_count = t_end - t_start
        print('[花費時間]', t_count)

        return wrap

    @timer
    def dosomething():
        print('do some thing')

    dosomething()

    print(dosomething.__name__)
    # >> > wrap

# ****************************************************************************************************

# 如果要消除這個副作用的話，可以使用 python 內建的 functools
#
# 只需要在 def wrap()之前，加上 @wraps(func)，即可獲得原先的 name 屬性 dosomething。
#
# 如下：
from functools import wraps
import time


def timer(func):
    @wraps(func)
    def wrap():
        t_start = time.time()
        func()
        t_end = time.time()
        t_count = t_end - t_start
        print('[花費時間]', t_count)

        return wrap

    @timer
    def dosomething():
        print('do some thing')

    dosomething()

    print(dosomething.__name__)
    # >> > dosomething

# ****************************************************************************************************

# 出現多個語法糖的時候
# 裝飾詞(語法糖)的觸發先後順序
#
# 上面程式只有加入一個語法糖，所以不難判斷執行流程
#
# 那如果加入很多個呢?
#
# A：執行順序會由上而下執行
#
# 以下範例：
from functools import wraps
import time


def timer(func):
    @wraps(func)
    def wrap():
        t_start = time.time()
        func()
        t_end = time.time()
        t_count = t_end - t_start
        print('[花費時間]', t_count)

        return wrap

    def func_print_one(func):
        @wraps(func)
        def wrap():
            print('this is func_print_one')
            func()

        return wrap

    def func_print_two(func):
        @wraps(func)
        def wrap():
            print('this is func_print_two')
            func()

        return wrap

    @timer
    @func_print_one
    @func_print_two
    def dosomething():
        print('do some thing')

    dosomething()
    # ff = timer(func_print_one(func_print_two(dosomething)))

# ff 是不使用語法糖，用包裝函式來還原的指令
#
# 按照執行順序會由上而下執行的概念，位置越上面的語法糖，會在越外層