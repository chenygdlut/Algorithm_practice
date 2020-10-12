'''
LC 47
给定一个可包含重复数字的序列，返回所有不重复的全排列。
'''
def permute2(nums):
    ans=[]
    nums.sort()
    check=[0 for i in range(len(nums))]
    def back(temp,check):
        if len(temp)==len(nums):
            ans.append(temp)
            return
        for i in range(len(nums)):
            if check[i]==1:
                continue
            if i>0 and nums[i]==nums[i-1] and check[i-1]==0:  # 前一个元素未被访问 且当前元素与前一个相同 跳过当前元素（不与前一个元素重复）
                continue
            check[i]=1
            back(temp+[nums[i]],check)
            check[i]=0
    back([],check)
    return ans

print(permute2([1,1,2]))