list1 = [1 , 2 , 3 , 4 , 5 , 6]      #建立串列

print("List1 = " , list1)        #顯示串列

print("List1的第一個元素 = " , list1[0])      #顯示串列中第一個元素(編號0)

print("List1的最後一個元素 = " , list1[-1])      #顯示串列中最後一個元素(編號-1)

print("List1中，索引值 2 ~ 4 的元素(不包含4) = " , list1[2 : 4])        #切割索引值 2 ~ 4 的元素(不包含4)

print("List1中，索引值 2 ~ 最後 的元素 " , list1[2 :])        #切割索引值 2 ~ 最後的元素

print("List1中，索引值 開始 ~ 5 的元素(不包含5) " , list1[: 5 ])        #切割索引值 開始 ~ 5 的元素(不包含5)

print(" ")


print("=====指定串列內的元素=====")
list1[0] = 99       #指定串列內的元素
print("List1 = " , list1)
print(" ")

print("========新增(append、insert)元素========")
list1.append(15)        #新增(append)，元素只能新增在最後位置
print("使用append功能，List1 = " , list1)
print(" ")

list1.insert(0 , 15)        #新增(insert)，元素可指定新增位置
print("使用insert功能，List1 = " , list1)
print(" ")

print("========移除(pop、remove)元素========")
list1.pop()     #移除(pop)，如果沒指定參數，將移除最後位置的元素
print("使用pop功能(未指定參數)，List1 = " , list1)
print(" ")

list1.pop(3)     #移除(pop)，如果有指定參數，則移除指定位置的元素
print("使用pop功能(有指定參數)，List1 = " , list1)
print(" ")

list1.remove(99)        #移除(remove)，移除指定資料，如果內部無指定資料，則報錯
print("使用remove功能，List1 = " , list1)
print(" ")

# **********************************************************************************

#走訪串列

#取出每一個項目
list1 = [1 , 2 , 3 ,4 , 5 , 6]
for i in list1:
    print("i = " , i)
print(" ")

#取出每一個項目和索引值，enumerate(index , 元素)
for index , i in enumerate(list1):
    print("index = " , index , "   " , "i = " , i)


# **********************************************************************************

# 使用append函數
list1 = []
for i in range(10):
    list1.append(i)
print("List1 = " , list1)       #顯示全部
print(" ")


list1 = []
for i in range(10):
    if i % 2 == 0:      #只顯示偶數項
        list1.append(i)
print("List1 = " , list1)
print(" ")

print("===========================")

# 使用"串列生成式"語法
list1 = [i for i in range(10)]
print("List1 = " , list1)       #顯示全部
print(" ")

list1 = [i for i in range(10) if i % 2 == 0 ]
print("List1 = " , list1)       #只顯示偶數項
print(" ")

# **********************************************************************************

# 字典

d = {"zero" : 0 , "one" : 1 , "two" : 2}

print("顯示鍵zero的值 = " , d["zero"])        #使用Key取得值
print(" ")

print("是否存在指定key：" , "zero" in d)      #確認是否存在指定Key，是則True,否則False
print(" ")

d["three"] = 3      #新增元素
print("新增鍵three之後 = " , d)
print(" ")

print("鍵zero的值 = ",d.get("zero"))        #get指令，取出指定鍵的值，如果不存在則顯示"None"
print(" ")

del d["zero"]       #刪除指定鍵和值
print("刪除鍵zero之後 = " , d)


# **********************************************************************************

#走訪字典

#走訪所有鍵，並顯示值
d = {"zero" : 0 , "one" : 1 , "two" : 2}

for key in d:
    value = d[key]
    print("key = " , key ,"   ","value = ", value)

print(" ")


#走訪所有鍵與值，item()
for key , value in d.items():
    print("key = ", key, "   ", "value = ", value)

print(" ")

# **********************************************************************************

#字典生成式

d = {i : i * i for i in range(10)}
print(d)


# **********************************************************************************

#集合

s = {"zero" , "two" , "three"}
print(s)
print(" ")

print("zero是否存在：","zero" in s)      #檢查元素是否存在於集合中，是則True,否則False
print(" ")

s.add("four")       #新增元素
print("新增元素後：" , s)
print(" ")

print("集合s的長度 = " , len(s))       #顯示集合長度
print(" ")

s.remove("two")        #刪除元素
print("刪除元素後：", s)

# **********************************************************************************

#走訪集合

s = {"zero" , "two" , "three"}
for index , ele in enumerate(s):
    print("#",index + 1 , ":" , ele)

# **********************************************************************************

#集合運算

a = {1 , 2 , 3 , 4 , 5 , 6}
b = {2 , 4 , 6 , 8 , 10 , 12}

print("交集：" , a & b)        # &：交集，表示多個集合內共同存在的元素
print(" ")

print("聯集：" , a|b)      # | ：聯集，表示多格集合內，所有不重複的元素
print(" ")

print("差集a - b：" , a - b)       # - ：差集，a - b為只存在於集合a，但不存在於集合b
print("差集b - a：" , b - a)       # - ：差集，b - a為只存在於集合b，但不存在於集合a
print(" ")

print("對稱差集：" , a ^ b)      # ^ ：對稱差集，表示不包含多個集合都擁有的元素

# **********************************************************************************