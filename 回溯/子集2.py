'''
LC 90
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。
'''
def subset2(nums):
    ans=[]
    nums.sort()  #先将数组进行排序
    def back(temp,cur):
        ans.append(temp)
        if cur==len(nums):
            return
        for i in range(cur,len(nums)):
            if i>cur and nums[i]==nums[i-1]:  #不能包括重复元素，需要跳过
                continue
            back(temp+[nums[i]],i+1)
    back([],0)
    return ans

print(subset2([4,4,4,1,2,3]))
