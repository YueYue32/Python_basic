# lambda function 匿名函式：用於快速建立function，不須給出function一個名稱
#
# lambda 後面放入想要操作的參數，參數可以不只有一個
#
# 「:」後面放的就是我們想要做的操作，即我們想要回傳的結果
#
# 最後再將整個lambda function指定存到一個變數a
#
#  重點觀念：把lambda函式一同放入變數，後續給定參數用法如下，用小括號()，包住想給定的值

a = lambda x,y: x+y

print(a(1,87))

# ***********************************************************************************************************

#計算兩人的年紀差
def difage(m,n): #the identifier is difage.
    return abs(m-n)

age=lambda x,y: abs(x-y)
#這個並非命名，而是將lambda存到一個變數age裡面

print('using function:{}'.format(difage(18,22)))
print('using lambda:{}'.format(age(18,22)))

# ***********************************************************************************************************

def squ_m(m): #the identifier is difage.
    return lambda x: m**x

pre_ans=squ_m(3)
#這裡我們用pre_ans用來接squ_m(m)這個function回傳回來的變數。因此，pre_ans即儲存lambda x: m^x
#所以接下來的操作就是lambda function的操作，利用變數pre_ans

print('3^5:{}'.format(pre_ans(5)))
print('3^3:{}'.format(pre_ans(3)))
pre_ans=squ_m(5)
print('5^3:{}'.format(pre_ans(3)))