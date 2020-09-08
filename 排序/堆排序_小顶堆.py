#以小顶堆为例、从大到小排
def HeapAdjust(List, i, length):  
    left = i*2+1
    right = i*2+2
    small = i
    if left<length and List[small]>List[left]:
        small = left
    if right<length and List[small]>List[right]:
        small = right
    if small != i:
        List[small], List[i] = List[i], List[small]
        HeapAdjust(List, small, length)

def buildHeap(List, N):
    for i in range(N//2, -1, -1):
        HeapAdjust(List, i, N)

def HeapSort(List, N):
    buildHeap(List, N)
    for i in range(N-1, -1, -1):
        List[0], List[i] = List[i], List[0]
        N -= 1
        HeapAdjust(List, 0, N)
    return List

if __name__=='__main__':
    d_ori = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
    d_right = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]
    N = len(d_ori)
    d_new_desc = HeapSort(d_ori,N) #从大到小排
    d_right.reverse()
    
    print(d_new_desc)
    print(d_right)
