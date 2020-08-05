'''
请设计一个算法，给一个字符串进行二进制编码，使得编码后字符串的长度最短。
'''
import sys
import heapq

#设赫夫曼树类
class Huffman:
    def __init__(self,val,char='NULL'):
        self.val=val
        self.left=None
        self.right=None
        self.char=char
    def __lt__(self,other):  #为了优先队列中可以进行元素比较改写比较函数
        return self.val<other.val

while True:  ##注意要设置循环输入格式，否则可能会与目标输出不同
    S=sys.stdin.readline().strip()
    if S=='':
        break
    dic={}
    for c in S:
        if c not in dic:
            dic[c]=1
        else:
            dic[c]+=1
    heap=[]

    i=0
    for k in dic:
        node=Huffman(dic[k],k)
        heapq.heappush(heap,node)

    while len(heap)>1:
        node1=heapq.heappop(heap)
        node2=heapq.heappop(heap)
        father=Huffman(node1.val+node2.val)
        father.left=node1
        father.right=node2
        heapq.heappush(heap, father)

    root=heapq.heappop(heap)

    #对霍夫曼树遍历计算编码长度
    def compute(node,height):
        if node.char!='NULL':
            return dic[node.char]*height
        left=compute(node.left,height+1)
        right=compute(node.right,height+1)
        return left+right

    print(compute(root,0))



