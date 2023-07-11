# 元組沒有生成式的語法，但是有類似的方式可以生成元組
#
# 範例：
a = tuple(i for i in range(10))
print(a)   # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

b = tuple(i*i for i in range(10) if i > 5)
print(b)   # (36, 49, 64, 81)