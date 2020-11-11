import random
r = random.randint(1,100)
while True:
	user_input = int(input("請輸入一個１～１００的整數："))
	if(user_input > r):
		print("再小一點")
	elif(user_input < r):
		print("再大一點")
	else:
		print("SUCCESS!!")
		break
	
