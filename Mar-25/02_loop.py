num1 = 3 
num2 = 7


max = num1 if(num1>num2) else num2

while True:

	if max % num1 == 0 and max % num2==0:
		print("LCM : ",max)
		break
	else:
		max = max+1
	
	
