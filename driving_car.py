driving = input('您有開過車嗎？ ')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	#強制終止
	raise SystemExit
age = input('請問您的年齡？ ')
age = int(age)
if driving == '有':
	if age >= 18:
		print('恭喜通過測驗')
	else:
		print('已經聯絡警察局')
elif driving == '沒有':
	if age >= 18 :
		print('快去考駕照')
	else:
		print('沒關係，再過')
		print(18 - age)
		print('年，就可以考駕照囉')