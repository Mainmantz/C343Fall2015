def swap(A,i,j):
	tmp = A[i]
	A[i] = A[j]
	A[j] = tmp

def swap_range(A,b1,b2,k):
	for i in range(k):
		swap(A,b1,b2)
		b1 = b1+1
		b2 = b2+1
	

		
	


A = [1,2,3,4,5,6,7,8,9]

swap_range(A,2,5,3)

#A = [1,2,6,7,8,3,4,5,9]

print A