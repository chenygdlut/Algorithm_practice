'''
查找矩阵中具有几个目标单词。
'''
loc=[[0,1],[0,-1],[1,0],[-1,0]]
def search(board,word,index,x,y,m,n,visited,ans):
    if index==len(word)-1:
        if board[x][y]==word[index]:
            ans+=1
        return ans
    if board[x][y]==word[index]:
        visited[x][y]=1
        for l in loc:
            newx,newy=x+l[0],y+l[1]
            if 0<=newx<m and 0<=newy<n and visited[newx][newy]==0 :
                ans=search(board,word,index+1,newx,newy,m,n,visited,ans)
        visited[x][y]=0
    return ans

def exist( board, word):
    m=len(board)
    n=len(board[0])
    visited=[[0 for i in range(n)] for j in range(m)]
    ans=0
    for i in range(m):
        for j in range(n):
            ans=search(board,word,0,i,j,m,n,visited,ans)
    return ans

board=[ ["C","H","I","E"],\
        ["S","I","N","A"],\
        ["A","D","A","E"]]
word="CHINA"
print(exist(board,word))