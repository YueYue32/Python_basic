# 使用Request送出HTTP請求
# `送出HTTP請求：`
#
# 在”Ruquest”套件中使用"get()"函數來送出GET請求。
import requests

r = requests.get("https://www.google.com")

print(r.status_code)

# 執行結果顯示"200"表示請求成功，如果值顯示"400~599"表示有錯誤，例如顯示”404”表示網頁不在。

# ********************************************************************************************************

# `送出POST請求：`
#
# POST請求就是送出HTML表單欄位的輸入資料。

import requests

post_data = {'name ' : "吳" , 'score': 95}

r = requests.post("https://httpbin.org/post" , data=post_data)

print(r.text)

#建立字典的送出資料post_data，在post()函數指定data參數是post_data的變數值，r.text屬性顯示回應字串，執行結果可以看到送出的name和score資料

# ********************************************************************************************************

# `檢視HTTP標頭資訊：`
#
# 使用Chrome瀏覽器的開發人員工具來檢視HTTP標頭資訊，以下為步驟說明：
#
# 1. 啟動Chrome瀏覽器進入”https://www.flag.com.tw/”(範例：旗標科技網站)
# 2.
# 3. 按”F12”開啟開發人員工具，按"F5"重新載入網頁，在上方選”Network”標籤下的"ALL"，可以看到完整HTTP請求清單
