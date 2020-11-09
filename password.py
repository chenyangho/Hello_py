password = "a123456"
chance = 3
while chance > 0:
	user_check = input("your password : ")
	if password == user_check:
		print("access")
		break
	else:
		chance -= 1
		print("wrong !! last", chance, "time!!")