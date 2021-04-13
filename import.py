import random
b = input('請輸入上限 ')
s = input('請輸入下限 ')
b = int(b)
s = int(s)
r = random.randint(s,b)
count = 0
while True:
	num = input('輸入數字 ')
	num = int(num)
	if num <= b and num >= s:
		count += 1
		if num < r:
			print('比答案小')
		elif num > r:
			print('比答案大')
		else:
			print('答對了 ','你總共猜了', count, '次')
			break
	else:
		print('是不是在哭')	

