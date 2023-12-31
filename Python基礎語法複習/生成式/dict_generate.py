# 範例1.
# 建立 “數值：數值平方” 的字典
# 單純寫法
a = {}
for i in range(1,10):
    a[i] = i*i   # 將 i*i 對應指定的鍵
print(a)         # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# 使用字典生成式
a = {i:i*i for i in range(1,10)}
print(a)       # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


