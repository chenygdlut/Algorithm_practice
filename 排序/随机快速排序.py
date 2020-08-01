#在快排基础上加入了随机选择枢点pivot的步骤（random_partition），其余与快排相同。
import random
def partition(List, left, right):
    temp=List[left]
    while left<right:
        while left<right and List[right]>=temp:
            right-=1
        if left<right:
            List[left]=List[right]
        while left<right and List[left]<=temp:
            left+=1
        if left<right:
            List[right]=List[left]
    List[left]=temp
    return left

def random_partition(List, left, right):
    rand = random.randint(left,right)
    # print(rand)
    List[left],List[rand] = List[rand],List[left]
    return partition(List,left,right)

def Qsort(List, left, right,L):
    # print(L,List,left,right)
    L+=1
    if left<right:
        loc=random_partition(List,left,right)
        List = Qsort(List,left,loc-1,L)
        List = Qsort(List,loc+1,right,L)
    return List


if __name__=='__main__':
    d_ori = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
    d_right = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]
    N = len(d_ori)
    L=0
    d_new = Qsort(d_ori,0,N-1,L)
    print(d_new)
    print(d_right)

