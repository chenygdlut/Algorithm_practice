'''
LC 77
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
'''
def combine(n, k):
    ans=[]
    def back(start,temp):
        if len(temp)==k:
            ans.append(temp)
            return
        for i in range(start,n+1):
            back(i+1,temp+[i])
    back(1,[])
    return ans

print(combine(4,2))