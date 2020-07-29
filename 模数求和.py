'''
现给定n个整数，并定义一个非负整数m，且令f(m) = (m%a1)+(m%a2)+...+(m%an)。
此处的X % Y的结果为X除以Y的余数。
现请你找出一个m，求出f(m)的最大值。
'''
import sys
from functools import reduce
def gcd(a,b):  # 递归求最大公约数
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
def get_lcm(L): #求一个列表中多个数的最小公倍数
    def lcm(a,b):  #求最小公倍数 ab之积除以最大公约数
        gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
        return a*b//gcd(a,b) 
    return reduce(lcm,L)  #reduce() 函数会对参数序列中元素进行计算累积，[3,4,5]：先对3,4进行函数计算，再对result和5进行计算。
line=sys.stdin.readline().strip()
n=int(line)
line=sys.stdin.readline().strip().split()
L=[int(s) for s in line]
M=get_lcm(L)-1
ans=0
for i in L:
    ans+=M%i
print(ans)