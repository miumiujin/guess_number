import random #輸入模組

r = random.randint(1,100)
count = 0 #這時候我們希望可以一邊猜一邊顯示猜幾次，不能放在while迴圈裡面，不然會一直被歸零
while True : #這時候不知道要設什麼，先設一個無限回圈
	count +=1 #等價於count = count + 1
	number = input("請猜數字 : ")
	number = int(number)  # casting(型別轉換)，將number轉成整數再儲存回去
	if number == r:
		print("恭喜猜對了~~")
		print("這是你猜的第", count, "次") #最後才補上的
		break #逃出迴圈
	elif number > r:
		print("比答案大!")
	elif number < r:
		print("比答案小QQ")
	print("這是你猜的第", count, "次") #逗點後面加上空格，視覺上比較美觀

#觀察實際運行結果 : 我們在猜對的時候並沒有顯示這是猜的第幾次
#比較原始的程式碼可以發現這是因為當我們猜對的時候就跑出迴圈了，所以不會執行到最後一行的 print
