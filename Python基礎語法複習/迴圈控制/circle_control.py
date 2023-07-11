# While
a = int(input("Enter a number = "))

r = 1
n = 1

while n <= a:
    r = r * n
    n += 1

print("階乘值 = " , r)


# ******************************************

# break
a = 1
while True:
    print("a = " , a )
    a = a + 1
    if a > 5 :      #當滿足a > 5這條件時，跳出迴圈
        break

# ******************************************

# continue
#當i 除以2後的餘數等於1時，繼續執行迴圈而不print(所以奇數不會被印出)

for i in range(1, 20):
    if i % 2 == 1:
        continue
    print("i = " , i)
