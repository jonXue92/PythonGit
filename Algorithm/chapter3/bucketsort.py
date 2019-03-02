# -*- coding: utf-8 -*-

import math
def sort(a, radix=10):
    """a为整数列表， radix为基数"""
    K = int(math.ceil(math.log(max(a)+1, radix))) # 用K位数可表示任意整数
    for i in range(1, K+1): # K次循环
        bucket = [[] for i in range(radix)] # 不能用 [[]]*radix，否则相当于开了radix个完全相同的list对象
        for val in a:
            bucket[val%(radix**i)//(radix**(i-1))].append(val) # 獲得整數第K位數字 （從低到高）
        del a[:]
        for each in bucket:
            a.extend(each) # 桶合并