# for i in range(10):
# 	print(i) 

# for i in range(12  , 18):
# 	print(i)

# for i in range(10,1, -1):
# 	print(i)
# tech = "Python"
# for chrs in range(0,len(tech)):
# 	print(tech[chrs])
# for x in tech:
# 	print(x)

# num = 15
# count = 0
# for i in range(1,num+1):
# 	rem = num%i 
# 	if(rem == 0):
# 		count = count +1
# if(count > 1):
# 	print("%d is composite as %d has %d factors"%(num , num , count))
# else:
# 	print("%d is Prime"%(num))

# for num in range(1,100):
# 	count = 0
# 	for i in range(1,num+1):
# 		rem = num%i 
# 		if(rem == 0):
# 			count = count +1
# 	if(count > 2):
# 		print("%d is composite as %d has %d factors"%(num , num , count))
# 	else:
# 		print("%d is Prime"%(num)) 
# n =5
# for i in range(0,n+1):
# 	for j in range(0,i+1):
# 		print("*" * j)


n=5
for i in range(0,n+1):
	for j in range(0,i):
		print("1" * j)