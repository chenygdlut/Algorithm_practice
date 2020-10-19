def minDistance(word1, word2):
    M=len(word1)
    N=len(word2)
    dp=[[float('inf') for i in range(N+1)] for j in range(M+1)]  #考虑开始字符#

    dp[0][0]=0  #两个空串则编辑距离为0

    # 边界表示空串与一个字符串之间的编辑距离
    for i in range(1,M+1):
        dp[i][0]=i
    for j in range(1,N+1):
        dp[0][j]=j
    
    # 分情况讨论，如果两个字母相同，则为添加(不使用当前的相等条件)或替换-1(使用当前的相等条件，即相等的字符不需要替换)中的最小值+1，添加为dp[i][j+1],dp[i+1][j]，替换为dp[i][j]-1
    # 如果两个字母不同，则为添加或替换中的最小值+1，添加为dp[i][j+1],删除为dp[i+1][j]，替换为dp[i][j]
    for i in range(M):
        for j in range(N):
            if word1[i]==word2[j]:
                dp[i+1][j+1]=min(dp[i][j]-1,dp[i][j+1],dp[i+1][j])+1
            else:
                dp[i+1][j+1]=min(dp[i][j],dp[i][j+1],dp[i+1][j])+1
    return dp[M][N]