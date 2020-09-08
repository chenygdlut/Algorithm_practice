'''给定二叉树层次遍历序列，构建二叉树'''
List=[1,2,3,4,'#','#','#','#',5,'#','#','#','#','#','#','#','#',6]
# print(len(List))
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def build(i):
    if i>=len(List):
        return None
    if List[i]=='#':
        return None
    root=TreeNode(List[i])
    root.left=build(i*2+1)
    root.right=build(i*2+2)
    return root

def showTree(root):
    queue=[root]
    while len(queue)>0:
        length=len(queue)
        temp=[]
        while length>0:
            node=queue.pop(0)
            length-=1
            if node!=0:
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(0)
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(0)
            else:
                temp.append(0)
                queue.append(0)
                queue.append(0)
        if temp.count(0)==len(temp):
            break
        print(temp)

showTree(build(0))

