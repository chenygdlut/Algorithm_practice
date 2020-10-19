'''
蓄水池采样：给定一个数据流，数据流长度N很大，且N直到处理完所有数据之前都不可知，请问如何在只遍历一遍数据（O(N)）的情况下，能够随机选取出m个不重复的数据。
在不知道总数的情况下，还需要采样概率相同。蓄水池大小为m，即采样m个样本；假设总样本数为N，实际不知道N的具体数值。
在i<=m时，直接采样；在i>m时，以一定的概率计算是否使用当前数据对已采样的数据进行替换，替换的概率是1/(i+1)，保留的概率是i/i+1；最后原i<=m的数据保留的概率是m/N，原i>m的数据保留的概率是m/i*i/N=m/N。
'''
import random
N=100
m=10
dataStream=[i for i in range(N)]
reservoir=[-1 for i in range(m)]
for i in range(m):
    reservoir[i]=dataStream[i]

for i in range(m,N):
    d=random.randint(0,i+1)
    if d<m:
        reservoir[d]=dataStream[i]
    
print(reservoir)
