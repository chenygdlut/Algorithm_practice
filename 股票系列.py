"""
买卖一次
"""
def maxProfit1(prices):
    ans=0
    curmin=float('inf')
    for i in prices:
        ans=max(ans,i-curmin)
        curmin=min(curmin,i)
    return ans

print(maxProfit1([7,1,5,3,6,4]))

"""
买卖多次
"""
def maxProfit2(prices):
    if len(prices)==0:
        return 0
    hold=-prices[0]
    cash=0
    
    prehold,precash=hold,cash
    for i in range(1,len(prices)):
        hold=max(prehold,precash-prices[i])
        cash=max(precash,prehold+prices[i])

        prehold,precash=hold,cash
    return cash

print(maxProfit2([7,1,5,3,6,4]))

"""
买卖多次 含手续费
"""
def maxProfit3(prices,fee):
    if len(prices)==0:
        return 0
    hold=-prices[0]
    cash=0
    
    prehold,precash=hold,cash
    for i in range(1,len(prices)):
        hold=max(prehold,precash-prices[i])
        cash=max(precash,prehold+prices[i]-fee)

        prehold,precash=hold,cash
    return cash

print(maxProfit3([1, 3, 2, 8, 4, 9],2))

"""
买卖多次 含冷冻期（1天）
"""
def maxProfit4(prices):
    if len(prices)==0:
        return 0
    hold=-prices[0]
    cash_nofreeze=0 # 冷冻期后
    cash_freeze=0  # 冷冻期内
    
    prehold,precash_nofreeze,precash_freeze=hold,cash_nofreeze,cash_freeze
    for i in range(1,len(prices)):
        hold=max(prehold,precash_nofreeze-prices[i])
        cash_nofreeze=max(precash_nofreeze,precash_freeze)
        cash_freeze=prehold+prices[i]

        prehold,precash_nofreeze,precash_freeze=hold,cash_nofreeze,cash_freeze
    return max(cash_freeze,cash_nofreeze)

print(maxProfit4([1,2,3,0,2]))


"""
买卖k次 
"""
def maxProfit5(prices,k):
    if len(prices)==0:
        return 0
    n=len(prices)
    if k<n/2:
        hold=[[float('-inf')for i in range(n)]for j in range(k+1)]
        cash=[[0 for i in range(n)]for j in range(k+1)]

        for i in range(n):
            for j in range(k,0,-1):
                hold[j][i]=max(hold[j][i-1],cash[j-1][i-1]-prices[i])
                cash[j][i]=max(cash[j][i-1],hold[j][i-1]+prices[i])
        return cash[k][n-1]
    else:
        return maxProfit2(prices)

print(maxProfit5([3,2,6,5,0,3],2))

