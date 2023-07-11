import csv

list1 = ['2022-10-19','2022-10-18','2022-10-17']


with open('test.csv', 'w', newline='',encoding='UTF-8-sig') as test_file:

    for line in list1:
        test_file.write(line)
        test_file.write("\n")        #每輸入一筆就換行

#  **************************************************************************

import csv

list1 = ['2022-10-19','2022-10-18','2022-10-17']


with open('test.csv', 'w', newline='',encoding='UTF-8-sig') as test_file:

    writer = csv.writer(test_file)
    writer.writerow(list1)


#  **************************************************************************

import csv

list1 = ['2022-10-19','2022-10-18','2022-10-17']

list2 = []        #建議一空陣列


#將一維陣列改動成二維陣列
for i in list1:
    list2.append([i])
print("list1 = ", list1)
print("list2 = " , list2)


with open('csvfile.csv','w', newline='',encoding='UTF-8-sig') as file:
    writer = csv.writer(file)
    for i in list2:
        writer.writerow(i)