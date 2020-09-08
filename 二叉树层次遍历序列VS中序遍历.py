'''
由层次遍历序列求某点的中序遍历下一个点
'''

def getNext(List,val):
    length=len(List)
    idx=List.index(val)
    # 有右子树则返回右子树最左的结点
    if idx*2+2<length and List[idx*2+2]!='#':  
        x=idx*2+2
        while x*2+1<length and List[x*2+1]!='#':
            x=x*2+1
        return List[x]
    else:  # 无右子树则
        if idx%2==1:  # 当前节点是左孩子返回父节点
            return List[(idx-1)//2]
        else: # 当前节点是右孩子，则循环找作为左孩子的祖先节点，返回其父节点，若遍历到根节点则返回None
            x=(idx-2)//2
            while x>0 and x%2==0:
                x=(x-2)//2
            if x%2==1:
                return List[(x-1)//2]
            else:
                return None



List=[1,2,3,4,'#','#',8,'#',5,'#','#','#','#','#','#','#','#',6,7]
val=4  #target=6
print(getNext(List,7))