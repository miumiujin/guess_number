import random #輸入模組

r = random.randint(1,100)

while True : #這時候不知道要設什麼，先設一個無限回圈
	number = input("請猜數字 : ")
	number = int(number)  # casting(型別轉換)，將number轉成整數再儲存回去
	if number == r:
		print("恭喜猜對了~~")
		break #逃出迴圈
	elif number > r:
		print("比答案大!")
	elif number < r:
		print("比答案小QQ")