# 定義一個函數convert_to_f(c)，c為參數

def convert_to_f(c):
    f = (9.0 * c) / 5.0 + 32.0

    return f        #回傳執行結果


c = 10      #定義參數
tem = convert_to_f(c)       #呼叫函數
print(tem)

# ********************************************

# 匯入random套件，並使用套件內功能
import random

a = random.randint(1 , 10)

print("random number = " , a)


# ********************************************

#匯入numpy套件，改名並使用套件內功能
import numpy as np

a = np.arange(10)

print("Array = " , a)