def Function(name,mrp,discount=10):
	payable = round(mrp - (mrp*discount)/100)
	return payable,mrp

#dict... 
ans = Function(mrp=29.35,name = "Cipladine")
print(ans[0], ans[1])


