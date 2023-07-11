# 建立資料庫連線
dbhost = "localhost"        #連線主機名稱

dbuser = "root"        #登入帳號

dbpassword = "allen33323"        #登入密碼

dbname = "new_1"        #資料庫名稱

#在本機執行的話，前2項不須變動


#資料庫連線設定
db = pymysql.connect(host=dbhost , user=dbuser , password=dbpassword , database=dbname , charset="utf8")

#建立操作游標
cursor = db.cursor()

# **************************************************************************************************************

# 將資料陣列寫入CSV和資料庫
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# 先建立計數器和標題，計數器後續for迴圈使用
num = 0

header = [" ", "標題", "發布單位", "時間", "點閱數"]

# 建立一個CSV檔案(t2.csv)，裝入後續資料
with open('t2.csv', 'w', newline='', encoding='utf-8') as test_file:
    writer = csv.writer(test_file)  # 建立寫入指令
    writer.writerow(header)  # 寫入標題

    for line in list1:
        line.insert(0, num + 1)  # 新增編號(新增在每一筆資料的開頭)

        num += 1
        print("line = ", line)

        writer.writerow(line)

== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==

# 建立資料庫的"新增"語法(INSERT INTO)，每一個%s對應一個字串
# 資料數量和資料庫列數量要一致
sql = "INSERT INTO new_table VALUES (%s,%s,%s,%s,%s)"

# 執行語法
for i in list1:
    try:

        # 語法：sql = INSERT INTO <name> VALUES (%s,%s,%s,%s,%s)
        # cursor.execute(sql,資料)
        cursor.execute(sql, i)

        # 提交修改
        db.commit()

        # 每一次執行(寫入資料)成功，就印一筆success，success數量理論上等同於資料數量
        print('success')

    # 這邊不能放入close指令，不然每執行成功一次，就會中斷連線一次，後續資料便無法寫入
    # db.close()

    except pymysql.Error as e:
        # 發生錯誤時停止執行SQL
        db.rollback()
        print('error = ', str(e))

        # 全部執行完之後，再close
        db.close()