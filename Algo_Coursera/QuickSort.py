def main():
	L=[int(line.rstrip('\n')) for line in open('QuickSort-Array.txt')]
	def QS(L,left,right):
		if(right-left==0 | right-left ==-1):
			return 0
		p=left
		for i in range(left+1,right+1):
			if L[i]<L[p]:
				temp=L[i] 
				L[i]=L[p+1]   # three swaps : less efficient
				L[p+1]=L[p]
				L[p]=temp
				p=p+1	

		QS(L,left,p-1)
		QS(L,p+1,right)

	QS(L,0,len(L)-1)
	#print L


if __name__ == '__main__':
	import time
	start_time = time.time()
	main()
	print("--- %s seconds ---" % (time.time() - start_time))