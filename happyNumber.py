num=23

while(num/10>0):
	k=10
	tot=0
	while((num)>0):
		# print tot, num,k,num%k
		tot+=pow(num%k,2)
		num=num/k

	num=tot

print num==1

