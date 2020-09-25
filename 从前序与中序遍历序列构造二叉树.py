'''
LC 105 
根据一棵树的前序遍历与中序遍历构造二叉树。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def buildTree(preorder, inorder):
    def build(preleft,preright,inleft,inright):
        if preleft>preright:
            return None
        val=preorder[preleft]
        root=TreeNode(val)
        index=inorder.index(val)
        leftlength=index-inleft
        rightlength=inright-index
        root.left=build(preleft+1,preleft+leftlength,inleft,index-1)
        root.right=build(preleft+leftlength+1,preright,index+1,inright)
        return root
    
    return build(0,len(preorder)-1,0,len(inorder)-1)

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

preorder= [3,9,20,15,7]
inorder=[9,3,15,20,7]

print(showTree(buildTree(preorder,inorder)))