month = 10
date = 13

print("===更改型態前===")

print(type(month))
print(type(date))

print("===更改型態後===")

month = str(month)
date = str(date)

print(type(month))
print(type(date))

print("===字串連接===")

print("月份 = " , str(month))
print("日期 = " , str(date))