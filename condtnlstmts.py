# a =10 
# if(a==10):
# 	pass
# else:
# 	print("hello")
time = input("Please enter the time")
# time = 25
if(time>=0 and time<24):
	if(time<11 and time>6):
		print("G m")
	elif(time>11 and time<15):
		print("G a")
else:
	print("time is invalid")
