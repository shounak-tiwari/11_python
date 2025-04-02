# write a program for print bill of medicine with app disc and the default discount is 10% 
def payBill(name,mrp,discount=10):
	discount_rs = (mrp*discount)/100
	payable_amount = mrp-discount_rs
	return name,mrp,discount_rs,payable_amount
#tuple : can not modified 
amount = 0
while True:
	add_more =str(input("if : yes  else : no"))
	if add_more=="yes" or add_more =="y":
		name  = str(input("Enter the name of product : "))
		mrp  = float(input("Enter the mrp of product : "))
		payable = payBill(name,mrp)
		amount = amount +payable[3]
		print(f"product name : {payable[0]}")
		print(f"product mrp : {payable[1]}")
		print(f"product discount : {payable[2]}")
		print(f"product payable : {payable[3]}")
	else:
		print(f"payable amount : {amount}")
		break

