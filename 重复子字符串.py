'''
找两个字符串的所有公共子字符串。
eg：1234567890   0123634556
ans：0 123 345 56 6
'''
def find_substring(s1,s2):
    ans=[]
    m=len(s1)
    n=len(s2)
    temp=[[0 for _ in range(n)]for _ in range(m)]
    visited=[[0 for _ in range(n)]for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if s1[i]==s2[j]:
                temp[i][j]=1
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if temp[i][j]==1 and visited[i][j]==0:
                sub=''
                x,y=i,j
                while x>=0 and y>=0 and temp[x][y]==1:
                    sub=s1[x]+sub
                    visited[x][y]=1
                    x-=1
                    y-=1
                ans.append(sub)
    return ans

print(find_substring('1234567890','0123634556'))