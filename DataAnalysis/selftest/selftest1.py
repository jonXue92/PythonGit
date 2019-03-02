# -*- coding: utf-8 -*-

temp=input().split()
n=int(temp[0])
sign=temp[1]

i=1
while True:
    if (2*i*i-1) <= n < (2*i*i+4*i+1):
        cengshu=i
        shengyu=n-2*i*i+1
        break
    i+=1

#for i in list(range(cengshu))+list(range(cengshu-2,-1,-1)):
#  print(i*' '+(2*cengshu-1-2*i)*sign)
for i in range(1-cengshu,cengshu):
    print(' '*(cengshu-1-abs(i))+sign*(2*abs(i)+1))
print(shengyu)