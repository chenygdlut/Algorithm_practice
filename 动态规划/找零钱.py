'''
LC 322
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
'''
def coinchange1(coins,amount):
    dp=[float('inf') for i in range(amount+1)]
    dp[0]=0
    for i in range(1,amount+1):
        for c in coins:
            if i>=c:
                dp[i]=min(dp[i],dp[i-c]+1)
    if dp[amount]==float('inf'):
        return -1
    else:
        return dp[amount]

print(coinchange1([1, 2, 5],11))

'''
LC 518
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 
'''
def coinchange2(coins,amount):
    dp=[0 for i in range(amount+1)]
    dp[0]=1
    for c in coins:
        for i in range(1,amount+1):  # 正着动态规划
            if i>=c:
                dp[i]+=dp[i-c]
    return dp[amount]

print(coinchange2([1,2,5],5))