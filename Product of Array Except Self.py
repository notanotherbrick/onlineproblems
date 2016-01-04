def prodArray(L):
    temp=1
    for k in range(len(L)):
        temp=temp*L[k]
    return temp
nums=[1,2,3,4,5,6]#,5,6,7,8,9,10,11]

n=len(nums)
k=int(pow(n,0.5)) # length of each pair
k1=k-1
import math
npairs=int(math.ceil(n/float(k))) # no of pairs
subprod=[0]*npairs
result=[0]*n

temp=1
j=0 # intialize counter for subprod
for i in range(n):
    temp=temp*nums[i]
    if i%k==(k1):# fill subprod array
        subprod[j]=temp
        temp=1 # reset temp to 1
        j+=1
        
if j<npairs:
    subprod[j]=temp

for j in range(npairs-1): # no of pairs except last - edge case
    temp=prodArray(subprod[:j])*prodArray(subprod[j+1:])
    for i in range(k):
        temp2=prodArray(nums[(j*k):(j*k)+i])*prodArray(nums[(j*k)+i+1:k*(j+1)])
        #print j*k+i+1,"pre",nums[(j*k):(j*k)+i],temp2,"post",nums[(j*k)+i+1:k*(j+1)],temp3
        result[j*k+i]=temp*temp2

    temp=prodArray(subprod[:j])*prodArray(subprod[j+1:n])
i=
while(i<n):
    i+=1

print result

# deal for last pair here



print subprod