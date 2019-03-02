# -*- coding: utf-8 -*-

def sortColors(a):
    if not a:
        return
    
    pl, pr = 0, len(a)-1
    i = 0
    while i <= pr:
    #这里有一个实现上的小细节，当发现一个 0 丢到左边的时候，i需要++，
    #但是发现一个2 丢到右边的时候，i不用++。原因是，从pr 换过来的数有可能是0或者2，
    #需要继续判断丢到左边还是右边。而从 pl 换过来的数，要么是0要么是1，不需要再往右边丢了。
    #因此这里 i 指针还有一个角度可以理解为，i指针的左侧，都是0和1。
        if a[i] == 0:
            a[pl], a[i] = a[i], a[pl]
            pl += 1
            i += 1
        elif a[i] == 1:
            i += 1
        else:
            a[pr], a[i] = a[i], a[pr]
            pr -= 1