ans = 'a123456'
i = 3
while i > 0 :
	pas = input('請輸入密碼 ')
	i = i - 1
	if pas == ans:	
		break
	elif i > 0:
		print('輸入錯誤還剩下',i,'次機會')
if pas == ans:
	print('密碼正確')
else:
	print('失敗')