
def getNext(s,n,Next):
    j,k=0,-1
    Next[j]=k
    while j<n:
        if k==-1 or s[j]==s[k]:
            j+=1
            k+=1
            Next[j]=k
        else:
            k=Next[k]

s='abcac'
Next=[0 for i in range(len(s)+1)]
getNext(s,len(s),Next)
L=len(s)-Next[len(s)]

if len(s)%L==0:
    print(s[:L])
else:
    print(s)