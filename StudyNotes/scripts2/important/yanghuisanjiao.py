def triangles():
    a=[1]
    while True:
        yield a
        a.append(0)
        for i in range(len(a)-1,0,-1):
            a[i]=a[i]+a[i-1]

n=0
for t in triangles():
    print(t)
    n=n+1
    if n==10:
        break