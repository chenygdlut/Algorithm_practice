from collections import defaultdict
def ladderLength(beginWord,endWord,wordList):
    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0
    L=len(beginWord)
    dic=defaultdict(list)
    for word in wordList:
        for i in range(L):
            temp=word[:i]+'*'+word[i+1:]
            dic[temp].append(word)
    
    queue=[(beginWord,1)]
    visited=set()
    visited.add(beginWord)

    while queue:
        cur,level=queue.pop(0)
        for i in range(L):
            media=cur[:i]+'*'+cur[i+1:]
            for word in dic[media]:
                if word == endWord:
                    return level+1
                if word not in visited:
                    visited.add(word)
                    queue.append((word,level+1))
            dic[media]=[]
    return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(ladderLength(beginWord,endWord,wordList))