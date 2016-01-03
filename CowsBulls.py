secret='1807'
guess='7810'

count=[0]*10

bulls=0
cows=0

for i in range(len(secret)):
	if secret[i]==guess[i]:
		bulls+=1
	else:
#		print i,(secret[0]), int(guess[i])
		if count[int(secret[i])]<0:
			cows+=1
		count[int(secret[i])]+=1

		if count[int(guess[i])]>0:
			cows+=1

		count[int(guess[i])]-=1

return str(bulls)+"A"+str(cows)+"B"