'''
LC 40
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。
'''
def combinationSum2(candidates, target) :
    ans=[]
    candidates.sort()   # 事先将数组排序
    def back(temp,cur,target):
        if target==0:
            ans.append(temp)
        for i in range(cur,len(candidates)):
            if candidates[i]>target:  # 如果数组元素大于目标值则结束
                break
            if i>cur and candidates[i]==candidates[i-1]:  # 跳过当前层的重复元素，防止出现相同的组合
                continue
            back(temp+[candidates[i]],i+1,target-candidates[i])  # 回溯从下一个元素开始，每个数字在每个组合中只能使用一次
    back([],0,target)
    return ans

print(combinationSum2([10,1,2,7,6,1,5],8))