import math
def Merge(List,low,mid,high):
    left=List[low:mid]
    right=List[mid:high]
    result=[]
    x,y=0,0
    while x<len(left) and y<len(right):
        if left[x]<right[y]:
            result.append(left[x])
            x+=1
        else:
            result.append(right[y])
            y+=1
    result+=left[x:]
    result+=right[y:]
    List[low:high]=result

def Msort(List):
    i=1 #归并的粒度
    while i<len(List):
        low=0
        while low<len(List):
            mid=low+i
            high=min(mid+i,len(List))
            if mid<high:
                Merge(List,low,mid,high)
            low+=i*2
        i*=2

List=[23,52,67,6,18,10,11,2,36,17,29,33,14,69,15,27,1,90,66,13]
Msort(List)
print(List)