# Decorator
# 降低程式碼重複率
#
# 易讀性高
#
# 靈活度高

# https://www.maxlist.xyz/2019/12/07/python-decorator/
# https://dev.to/codemee/python-decorator-3bni

# ****************************************************************************************************************

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


def dosomething(sleep_time):
    print('do some thing')
    time.sleep(sleep_time)


foo = timer(dosomething)
foo(3)
# 等同 timer(dosomething)(3)

