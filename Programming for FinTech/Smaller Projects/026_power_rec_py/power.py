def power(x,y):
	if (y==0) : 
		return 1
	else:
		return(x*power(x, y-1))
print("Result=", power(0,0))