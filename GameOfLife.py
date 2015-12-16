import random
m = 5 
n = 3 
k=[]
k=[[0, 1, 0], [0, 1, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0]]
S=[]
S.append([])

for i in range(1,m-1):
	S.append([])
	for j in range(1,n-1):
		top=k[i+1][j]
  		bottom=k[i-1][j]
  		right=k[i][j+1]
  		left=k[i][j-1]
  		tl=k[i+1][j-1]
  		tr=k[i+1][j+1]
  		bl=k[i-1][j-1]
  		br=k[i-1][j+1]
  		h=top+bottom+left+right+tr+tl+bl+br
  		print i,j,h

  		if k[i][j]==1 & h<2:
  			S[i].append(0)
  		elif k[i][j]==1 & (h==2 or h==3):
  			S[i].append(1)
  		elif k[i][j] ==1 & (h>3):
  			S[i].append(0)
  		elif k[i][j]==0 & h==3:
  			S[i].append(1)
  		else:
  			S[i].append(k[i][j])

#  		k[i].append(int(round(random.random())))

print k,S


