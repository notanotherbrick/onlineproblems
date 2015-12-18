L=[9,9,9,9,9,8,4,4,4,4,4,4]
def QS(L,left,right):
	if(right-left==0):
		return
	p=left
	#isSorted=True
	for i in range(left+1,right+1):
		if L[i]<L[p]:
			temp=L[i] # L[i] needs to be shifted to left
			L[i]=L[p+1] # take value higher than 
			L[p+1]=L[p]
			L[p]=temp
			p=p+1
			# isSorted=False
			print L, "p is :",p, "i is :",i

	if(p==left):
	 	return
	else:
	 	QS(L,left,p)
	 	QS(L,p+1,right)

	#print L[left:right+1],p

QS(L,0,len(L)-1)
print L