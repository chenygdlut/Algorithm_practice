'''
LC 106 
根据一棵树的中序遍历与后序遍历构造二叉树。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def buildTree(inorder, postorder):
    dic={inorder[idx]:idx for idx in range(len(inorder))}
    def build(inleft,inright,postleft,postright):
        if postleft>postright:
            return None
        val=postorder[postright]
        root=TreeNode(val)
        index=dic[val]#inorder.index(val)
        leftlength=index-inleft
        rightlength=inright-index
        root.left=build(inleft,index-1,postleft,postleft+leftlength-1)
        root.right=build(index+1,inright,postleft+leftlength,postright-1)
        return root
    return build(0,len(inorder)-1,0,len(postorder)-1)

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


inorder=[9,3,15,20,7]
postorder=[9,15,7,20,3]

print(showTree(buildTree(inorder,postorder)))