# -*- coding: utf-8 -*-
def gcd(big, small):
    if small != 0:
        return gcd(small, big % small)
    else:
        return big
