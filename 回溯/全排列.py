'''
LC 46
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
'''
def permute(nums):
    ans=[]
    def back(temp,cur):
        if cur==len(nums):
            ans.append(temp[:])
        for i in range(cur,len(nums)):
            temp[i],temp[cur]=temp[cur],temp[i]
            back(temp,cur+1)
            temp[i],temp[cur]=temp[cur],temp[i]
    back(nums,0)
    return ans

print(permute([1,2,3]))
