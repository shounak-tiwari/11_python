# w a p for calculate the factorial of number using while/for

# 5*4*3*2*1

n = int(input("Enter the number : "))
temp = n
fact = 1
if n == 0 or n == 1:
	print(f"The factorial of {temp} : ",1)
else:
	while(n!=0):
		fact = fact*n 			# fact = 1*5
		n=n-1 					# n = 5-1
	else:
		print(f"The factorial of {temp} : ",fact)
