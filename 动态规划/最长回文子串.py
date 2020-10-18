'''
LC 5
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
'''
def longestPalindrome(s):
    n=len(s)
    ans=s[0]
    maxlen=1
    dp=[[False for i in range(n)] for j in range(n)]
    for i in range(n-2,-1,-1):
        dp[i][i]=True
        for j in range(i+1,n):
            if s[i]==s[j]:
                if i+1==j:
                    dp[i][j]=True
                else:
                    dp[i][j]|=dp[i+1][j-1]
            if dp[i][j]==True:
                if j-i+1>maxlen:
                    maxlen=j-i+1
                    ans=s[i:j+1]
    return ans

print(longestPalindrome('babad'))