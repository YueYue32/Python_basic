# 範例：
#
# 注意：由於是集合set，所以print出來的元素會是無序的(不按照順序)

a = set()
for i in range(1,10):
    a.add(i*i)   # 將 i*i 新增到集合裡
print(a)         # {64, 1, 4, 36, 9, 16, 49, 81, 25}

a = {i*i for i in range(1,10)}
print(a)       # {64, 1, 4, 36, 9, 16, 49, 81, 25}