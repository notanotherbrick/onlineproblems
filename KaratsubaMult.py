
def mult2nos(X,Y,n):
	if n<=1:
		return X*Y

	f=pow(10,n/2)
	a=X/f
	b=X%f
	c=Y/f
	d=Y%f

	ac=mult2nos(a,c,n/2)
	bd=mult2nos(b,d,n/2)
	mid=(a+b)(c+d)-ac-bd

	return (ac*pow(10,2*(n/2)))+bd+(mid*pow(10,n/2))


print "Hello"
X='101'
Y='3'
n=min(len(X),len(Y))
print mult2nos(int(X),int(Y),n-1)