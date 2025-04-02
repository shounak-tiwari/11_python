row = 1
while row<=5:
	space = 1
	while space <= row-1:
		print("_",end ="")
		space = space+1
	col=1
	while col<=6-row:
		print("*",end="")
		col = col+1
	print("")
	row= row+1
		
	 
