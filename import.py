import random
b = input('請輸入上限 ')
s = input('請輸入下限 ')
b = int(b)
s = int(s)
r = random.randint(s,b)

while True:
	num = input('輸入數字 ')
	num = int(num)
	if num < r:
		print('比答案小')
	elif num > r:
		print('比答案大')
	else:
		print('答對了')
		break
				

