'''
给定一个可能包含重复字符的字符串，给出所有字符的排列组合子串。

说明：解集不能包含重复的子串。
eg:XXY->{X,Y,XX,XY,YX,XXY,XYX,YXX}
'''
def substring(s):
    ans=[]
    visited=[0 for i in range(len(s))]      # 使用一维数组记录已访问过的元素
    def back(temp,visited):
        if len(temp)>0:
            ans.append(temp)
        if len(temp)==len(s):
            return
        used=set()
        for i in range(len(s)):
            if visited[i]==1 or s[i] in used:   # 事先未将字符串进行排序，使用哈希表跳过 当前层 已使用过的字符（目的是避免形成重复的字符串）
                continue
            visited[i]=1
            used.add(s[i])
            back(temp+s[i],visited)
            visited[i]=0            # 回溯时将已访问过的元素重置为未访问
    back('',visited)
    return ans

print(substring('XXY'))