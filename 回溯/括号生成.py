'''
LC 22
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
'''
def generateParenthesis(n):
    ans=[]
    def back(S,left,right):
        if len(S)==2*n:
            ans.append(''.join(S))
        if left<n:
            back(S+['('],left+1,right)
        if left>right:
            back(S+[')'],left,right+1)
    back([],0,0)
    return ans

print(generateParenthesis(3))