# https://steam.oxxostudio.tw/category/python/basic/comprehension.html

# **********************************************************************************************************

# 串列生成式

# 範例1.
# 單純寫法
a = []
for i in range(1, 10):
    a.append(i*i)
print("a = ", a)      # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 使用串列生成式
b = [j*j for j in range(1,10)]
print("b = ", b)      # [1, 4, 9, 16, 25, 36, 49, 64, 81]



# 範例2.
# 單純寫法
a = [10,20,30,40,50,60,70,80,90]
b = []
for i in a:
    b.append(max(a) - i)     # 用 a 的最大值減去每個項目
print(b)                   # [80, 70, 60, 50, 40, 30, 20, 10, 0]

# 使用串列生成式
a = [10,20,30,40,50,60,70,80,90]
b = [max(a)-i for i in a]
print(b)                   # [80, 70, 60, 50, 40, 30, 20, 10, 0]


# 範例3.
# 單純寫法
# 將兩層 for 迴圈的 i 和 j 加在一起，變成新串列的項目
a = []
for i in 'abc':
    for j in range(1,4):
        a.append(i + str(j))
print(a)        # ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

# 使用串列生成式
# 兩個 for 迴圈分別產生 i 和 j
a = [i + str(j) for i in 'abc' for j in range(1, 4)]
print(a)        # ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']


# 範例4.
# 單純寫法
a = [[100, 200, 300, 400, 500], [100, 200, 500, 2, 1]]
b = []
for i in a:
    b.append(min(i))  # 將二維串列中每個串列裡的最小值取出，變成新的串列
print(min(b))         # 1，印出新的串列裡的最小值

# 使用串列生成式
a = [[100, 200, 300, 400, 500], [100, 200, 500, 2, 1]]
print(min([min(i) for i in a]))   # 1



# 範例5.
# 單純寫法
a = []
for i in range(1,10):
    if i%2 == 0:
        a.append(i)   # 取出偶數放入變數 a
print(a)              # [2, 4, 6, 8]

# 使用串列生成式
a = [i for i in range(1, 10) if i%2 == 0]
print(a)           # [2, 4, 6, 8]


# 範例6.
# 如果將 if 放在 for 的前方，就必須加上 else
# 單純寫法
a = []
for i in range(1,10):
    if i%2 == 0:
        a.append(i)   # 取出偶數放入變數 a
    else:
        a.append(100) # 如果是奇數，將 100 放入變數 a
print(a)          # [100, 2, 100, 4, 100, 6, 100, 8, 100]

# 使用串列生成式
a = [i if i%2==0 else 100 for i in range(1, 10)]
print(a)          # [100, 2, 100, 4, 100, 6, 100, 8, 100]


