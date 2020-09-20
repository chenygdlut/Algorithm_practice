'''
LC 78
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。
'''
def subset(nums):
    ans=[]
    def back(temp,cur):
        ans.append(temp)
        if cur==len(nums):
            return
        for i in range(cur,len(nums)):
            back(temp+[nums[i]],i+1)
    back([],0)
    return ans

print(subset([2,1,4,3]))