# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:08:59 2018

@author: 薛正扬
"""
import math

def isPrime(num,box):
    for j in box:
        if (j <= math.sqrt(num) and num%j==0):
            return False
            break
    
n=int(input())

count=0
primes=[]
primes.append(2)
for i in range(3,n+1):
    if isPrime(i,primes) != False:
        if i - primes[-1] == 2:
            count+=1
        primes.append(i)

print(count)