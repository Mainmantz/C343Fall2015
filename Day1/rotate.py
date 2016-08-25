def rotate(x):
	for i in range(len(x)+1):
		if len(x) <= 1:
			return 
		else:
			last = x[len(x)-1]
			for i in range(len(x)-1,0,-1):
				x[i] = x[i-1]
			x[0] = last
		
	return x
			
			
			
print rotate([1,2,3,4,5])
