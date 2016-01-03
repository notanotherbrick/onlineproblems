n=5
x=0
y=0
z=0
count=0
p=[1]
while(count<n):
        nextUglyNum=min(min(2*p[x],3*p[y]),5*p[z])
        p.append(nextUglyNum)
        while(p[x]*2<=nextUglyNum):
                x+=1
        while(p[y]*3<=nextUglyNum):
                y+=1
        while(p[z]*5<=nextUglyNum):
                z+=1    
        count+=1
print p