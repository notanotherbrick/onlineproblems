def main():
	L=[int(line.rstrip('\n')) for line in open('QuickSort-Array.txt')]
	def QS(L,left,right):
		if(right-left==0 | right-left ==-1):
			return 0
		i=left+1
		for j in range(left+1,right+1):
			if L[j]<=L[left]:
				temp=L[j]
				L[j]=L[i]
				L[i]=temp
				i=i+1
				
		temp=L[i-1]
		L[i-1]=L[left]
		L[left]=temp
		QS(L,left,i-2)
		QS(L,i,right)

	QS(L,0,len(L)-1)
	#print L

if __name__ == '__main__':
	import time
	start_time = time.time()
	main()
	print("--- %s seconds ---" % (time.time() - start_time))