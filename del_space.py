'''
删除连续两个以上的空格至2个。
'''
def func(s):
    n=len(s)
    s=list(s)
    i=0
    count=0
    del_num=0
    while i<n:
        if s[i]!='-':
            count=0
            i+=1
            continue
        else:
            count+=1
            if count>2:
                j=i
                k=i
                while j<n-del_num and s[j]=='-':
                    j+=1
                del_num+=j-k
                s[k:k+n-j]=s[j:n]
            i+=1
    return ''.join(s[:n-del_num])

s='ab-s---------cde---------'
print(func(s))