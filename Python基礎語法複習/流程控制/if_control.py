# 單選條件控制
t = int(input("Please enter the temperature = "))

if t < 10:
    print("cold")

# ********************************************************

# 二選一條件控制
t = int(input("Please enter the temperature = "))

if t > 10:
    print("not cold")
else :
    print("cold")

# ********************************************************

# 多選一條件控制
t = int(input("Please enter the temperature = "))

if t > 20:
    print("hot")
elif 10 < t < 20:
    print("not cold")
else:
    print("cold")
    