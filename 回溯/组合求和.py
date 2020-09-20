'''
LC 39
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。
'''
def combinationSum(candidates, target):
    candidates.sort()  #将数组排序
    ans=[]
    def back(temp,cur,target):
        if target==0:
            ans.append(temp)
            return
        for i in range(cur,len(candidates)):
            if candidates[i]>target:  #如果数组元素大于当前值则结束
                break
            back(temp+[candidates[i]],i,target-candidates[i])  #每次回溯从当前元素开始（可以包含当前元素）
    back([],0,target)
    return ans
print(combinationSum([2,3,5],8))