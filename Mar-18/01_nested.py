#jee 
'''
1. age >=17 and age <=24
2. heigher sec is running or pass from more then 75%
'''
age = int(input("Enter the age of candidate : "))

if age>= 17 and age<=24:
	heigher_sec = str(input("Enter the heigher sec school marks or running of candidate : "))

	if heigher_sec =="running" or heigher_sec >="75%":
			print("Eligible for jee")
		


