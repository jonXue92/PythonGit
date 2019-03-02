# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 12:38:55 2018

@author: 薛正扬
"""
a=input().split()
b=input().split()
n=int(a[0])
m=int(a[1])

#切片(速度最快)
#m1=b[n-m:]
#m2=b[:n-m]
#x=m1+m2
#print(" ".join(x))

#算法：
def demo(lst,n,m):
    x=lst[:n-m]
    x.reverse()
    y=lst[n-m:]
    y.reverse()
    r=x+y
    return list(reversed(r))
print(" ".join(demo(b,n,m)))

#在前插入m个(慢)
#for i in range(m):
#    b.insert(0,b[n-1])
#del b[n:n+m]
#print(" ".join(b))

#在后插入n-m个(慢)
#if n>=m:
#    l=n-m
#else:
#    l=n-m%n
#for i in range(l):
#    x=b.pop(0)
#    b.append(x)
#print(" ".join(b))        

#将固定的某个位置的数字不断和它应当去的位置的数字交换,对于N个数字,移动M个位置,CYCLE=gcd(N,M)即为分组数,然后分CYCLE次循环移动各组内数字;每个组内移动 N/CYCLE-1次即可
#def gcd(n,m):
#    while n%m!=0:
#        gcd=n%m
#        n=m
#        m=gcd
#    return m

#if m>0:
#    cycle=gcd(n,m)
#else:
#    cycle=0
#for j in range(cycle):#组内循环
#    origin_last=j+1 #每个组内数据交换开始位置
#    step=int(n/cycle)
#    for i in range(1,step):
#        origin_next=(origin_last+m)%n ##计算将要交换数字的目的位置，注意此处数组编号从1开始计算
#        b[j],b[origin_next-1]=b[origin_next-1],b[j] #每当一组数据交换结束，j+1后开始下一组数据的交换
#        origin_last=origin_next #将刚被交换过来数字的原本位置更新，用于下一次交换
#message=''
#for number in b:
#    message+=number
#    message+=' '
#print(message.rstrip())