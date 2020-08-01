'''
牛牛有一个正整数x,牛牛需要把数字x中的数位进行重排得到一个新数(不同于x的数),牛牛想知道这个新数是否可能是原x的倍数。请你来帮他解决这个问题。
输入包括t+1行,第一行包括一个整数t(1 ≤ t ≤ 10),
接下来t行,每行一个整数x(1 ≤ x ≤ 10^6)
对于每个x,如果可能重排之后变为自己的倍数输出"Possible", 否则输出"Impossible".
'''
import sys
T=int(sys.stdin.readline().strip())
for i in range(T):
    line=sys.stdin.readline().strip()
    x=int(line)
    dic={}
    for c in line:
        if c in dic:
            dic[c]+=1
        else:
            dic[c]=1
            
    for a in range(2,10):
        flag=1
        newx=x*a
        newline=str(newx)
        dic_new=dic.copy()
        for c in newline:
            if c not in dic_new or dic_new[c]==0:
                flag=0
                break
            else:
                dic_new[c]-=1
            
        if flag==1:
            break
    if flag==1:
        print('Possible')
    else:
        print('Impossible')