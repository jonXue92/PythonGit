# -*- coding: utf-8 -*-

def power(x, n):
    ans = 1
    base = x
    while n > 0:
        if n % 2 == 1:
            ans *= base
        base *= base
        n = n // 2
    return ans