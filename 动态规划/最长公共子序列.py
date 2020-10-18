'''
LC 1143
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
'''
def longestCommonSubsequence(text1,text2):
    m=len(text1)
    n=len(text2)
    dp=[[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if text1[i-1]==text2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]

print(longestCommonSubsequence('abcde','ace'))


'''
返回具体的最长公共子序列内容。
'''
def longestCommonSubsequence(text1,text2):
    m=len(text1)
    n=len(text2)
    dp=[[0 for i in range(n+1)] for j in range(m+1)]
    memo=[[0 for i in range(n+1)]for j in range(m+1)]  #1:从i-1,j-1来  2:从i-1,j来  3:从i,j-1来
    for i in range(1,m+1):
        for j in range(1,n+1):
            if text1[i-1]==text2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
                memo[i][j]=1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                if dp[i-1][j]>dp[i][j-1]:
                    memo[i][j]=2
                else:
                    memo[i][j]=3
    
    ans=''
    x,y=m,n
    while x>0 and y>0:
        if memo[x][y]==1:
            ans=text1[x-1]+ans
            x-=1
            y-=1
        elif memo[x][y]==2:
            x-=1
        elif memo[x][y]==3:
            y-=1
    return ans

print(longestCommonSubsequence('abcde','ace'))
