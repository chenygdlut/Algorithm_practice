class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

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

def build(root,val):
    if root==None:
        root=TreeNode(val)
    elif val<root.val:
        root.left=build(root.left,val)
    elif val>root.val:
        root.right=build(root.right,val)
    return root

List=[33,54,12,45,65,24,100]
root=None
for i in List:
    root=build(root,i)
    
print(showTree(root))