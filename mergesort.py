

def mergesort(seq,left,right):
    if right-left==0: #or right-left ==1:
        return
    mid=(right+left)/2
    mergesort(seq,left,mid)
    mergesort(seq,mid+1,right)
    merge(seq,left,mid,right)
    
def merge(seq,left,mid,right):
    i=left
    j=mid+1
    k=0
    A=[0]*(right-left+1)
    while(i<=mid and j<=right):
        if(seq[i]<seq[j]):
           A[k]=seq[i]
           i+=1 
        elif(seq[i]>=seq[j]):
            A[k]=seq[j]
            j+=1
        #print k,A
        k+=1

    while(i<=mid):
        A[k]=seq[i]
        i+=1
        k+=1

    while(j<=right):
        A[k]=seq[j]
        j+=1
        k+=1
    seq[left:right+1]=A


S=[32,1,53,96,2,31,85,34,34,341,423,4311,32,341,41,56,23,5,6,2]
mergesort(S,0,len(S)-1)
print S
