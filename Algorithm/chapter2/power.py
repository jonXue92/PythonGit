# -*- coding: utf-8 -*-
def power(x, n):
    if n == 0:
        return 1
    
    if n % 2 == 0:
        tmp = power(x, n // 2)
        return tmp * tmp
    else:
        tmp = power(x, n // 2)
        return tmp * tmp * x
