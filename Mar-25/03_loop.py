# write a program for check number is prime or not 

number = int(input("Enter the number : ")) #997

i = 2

flag = 0

while (i<= number//2):
	if (number % i ==0 ):
		flag= flag + 1
		break
		
	i = i+1
		
print("number is prime") if(flag ==0 ) else print("number is not prime ")

