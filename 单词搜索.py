loc=[[0,1],[0,-1],[1,0],[-1,0]]
def search(board,word,index,x,y,m,n,visited):
        if index==len(word)-1:
            return board[x][y]==word[index]
        if board[x][y]==word[index]:
            visited[x][y]=1
            for l in loc:
                newx,newy=x+l[0],y+l[1]
                if 0<=newx<m and 0<=newy<n and visited[newx][newy]==0 :
                    if search(board,word,index+1,newx,newy,m,n,visited):
                        return True
            visited[x][y]=0
        return False

def exist( board, word):
    m=len(board)
    n=len(board[0])
    visited=[[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            if search(board,word,0,i,j,m,n,visited):
                return True
    return False

board=[ ["A","B","C","E"],\
        ["S","F","C","S"],\
        ["A","D","E","E"]]
word="ABCCED"
print(exist(board,word))