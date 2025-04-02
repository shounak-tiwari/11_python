#JEE
'''
1. age >=17 and age <=24
2. heigher sec is running or pass from more then 75%
'''
age = int(input("Enter The Age : "))

if age>=17 and age<=24:
    heigher_sec = str(input("Enter the 12th percentage or running status : "))
    if heigher_sec=="running" or heigher_sec>="75%":
        print("Yes ! candidate is eligible for JEE ")
    else:
        print("Oops! Candidate not eligible for JEE because heigher sec marks is not matched ")

else:
    print("Ooops ! Candidate age is not mathched please try Again if your age is between from 17 to 24 ")

