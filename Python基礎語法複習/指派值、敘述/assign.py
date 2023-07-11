#指定敘述

a = 10
b = 20
c = 30
d = 40

print("a = ",a ,",","b = ",b,"," ,"c = ",c ,",", "d= ",d)
print("")

#更改指派值

print("===c值指派給a、d值指派給b===")
a = c
b = d
print("a = ",a ,",","b = ",b,"," ,"c = ",c ,",", "d= ",d)
print("")

print("=======交換a、b兩值=======")
a , b = b , a
print("a = ",a ,",","b = ",b,"," ,"c = ",c ,",", "d= ",d)