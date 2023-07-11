# staticmethod
# Static method 靜態方法：不帶實例，不帶 class 為參數的方法

# https://www.learncodewithmike.com/2020/01/python-method.html

# ***********************************************************************************************************

# StaticMethods 使用方法：
#
# 在 def 函式上加上 @staticmethod
#
# 不用傳入 self 參數
#
# StaticMethods 使用時機：
#
# 不在需要將 class 實例後才能使用函式，直接像以下範例呼叫 People_StaticMethods.work(4) 即可使用
#
# 常用於 單純執行傳入參數或功能上運算的情況

# 汽車類別
class Cars:
    # 速率靜態方法
    @staticmethod
    def speed_rate(distance, minute):
        return distance / minute

# 透過物件呼叫
van = Cars()

van_rate = van.speed_rate(10000, 20)

print("van rate: ", van_rate)

# 透過類別呼叫
sports_car_rate = Cars.speed_rate(20000, 20)
print("sports car rate: ", sports_car_rate)

# ***********************************************************************************************************