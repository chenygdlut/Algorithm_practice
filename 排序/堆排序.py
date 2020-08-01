#以大顶堆为例
def HeapAdjust(List, i, length):
    left = i*2+1
    right = i*2+2
    large = i
    if left < length and List[left] > List[large]:
        large = left
    if right < length and List[right] > List[large]:
        large = right
    if large != i:
        List[large], List[i] = List[i], List[large]  #large!=i的时候才需要交换元素并继续调整堆
        List = HeapAdjust(List, large, length)
    
    return List

def buildHeap(List, N):
    for i in range(N//2, -1, -1):
        List = HeapAdjust(List, i, N)
    return List

def HeapSort(List, N):
    List = buildHeap(List, N)
    for i in range(N-1, -1, -1):
        List[0], List[i] = List[i], List[0]
        N -= 1
        List = HeapAdjust(List, 0, N)
    return List

if __name__=='__main__':
    d_ori = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
    d_right = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]
    N = len(d_ori)
    d_new = HeapSort(d_ori,N)
    print(d_new)
    print(d_right)
