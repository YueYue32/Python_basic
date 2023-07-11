# https://steam.oxxostudio.tw/category/python/basic/try-except.html

# *************************************************************************

# try、except：

# 當 try 區段內的程式發生錯誤時，就會執行 except 裡的內容

# 如果 try 的程式沒有錯誤，就不會執行 except 的內容


try:    # 使用 try，測試內容是否正確
    a = input('輸入數字：')
    print(a + 1)


except:     # 如果 try 的內容發生錯誤，就執行 except 裡的內容
    print('發生錯誤')

# *************************************************************************

# pass：

# 撰寫 try... except 有時候會遇到「不想做任何動作」的狀況 ( 連 print 都不想使用 )，這時可以使用 pass 語法來略過 ( 什麼事情都不做 )

# 以下方的程式而言，當發生錯誤時，進入 excpet 後就會直接忽略並跳過

try:    # 使用 try，測試內容是否正確
    a = input('輸入數字：')
    print(a + 1)


except:     # 如果 try 的內容發生錯誤，就執行 except 裡的內容
    pass

# *************************************************************************

# except Exception as e：

# 將所有的錯誤資訊全部印出

try:
    a = 1
    b = '1'
    print(a + b)

except Exception as e:
    print(e)

# *************************************************************************

# raise 、 assert：

# 在執行 try 的過程中，如果遇到需要「強制中斷」的情形，可使用 raise 強制中斷

# raise 後方可以加上錯誤資訊，錯誤資訊可以包含要呈現的訊息

try:
    a = int(input('輸入 0～9：'))
    if a > 10:
        raise ValueError('數字不在範圍內')

except ValueError as msg:    # 如果輸入範圍外的數字，執行這邊的程式
    print(msg)

except :                     # 如果輸入的不是數字，執行這邊的程式
    print('輸入非數字')

# *************************************************************************

# 使用 assert 中斷的方法為「assert False, '錯誤訊息'」，用法和 raise 類似，執行後就會中斷程式，並將錯誤資訊提供給 except 顯示

try:
    a = int(input('輸入 0～9：'))
    if a>10:
        assert False, '數字不在範圍內'

except AssertionError as msg:
    print(msg)

except :
    print('輸入非數字')

# *************************************************************************

# **else 、 finally：**

# 在 except 結束後，可以加入 else 或 finally 兩個額外的判斷

# else 表示完全沒有錯誤，就會執行該區塊的程式

# finally 則不論程式對錯，都會執行該區塊的程式

try:
    a = int(input('輸入 0～9：'))
    if a > 10:
        assert False, '數字不在範圍內'

except AssertionError as msg:
    print(msg)

except:
    print('輸入非數字')

else:
    print('沒有錯！繼續執行！')  # 完全沒錯才會執行這行

finally:
    print('管他有沒有錯，繼續啦！')  # 不論有沒有錯都會執行這行

# *************************************************************************