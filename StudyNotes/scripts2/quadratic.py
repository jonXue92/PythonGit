# -*- coding: utf-8 -*-

import math

def quadratic(a,b,c):
    if b*b - 4*a*c < 0:
        print('This equation has no real solution.')
    else:
        r1 = (- b + math.sqrt(b*b-4*a*c))/2/a
        r2 = (- b - math.sqrt(b*b-4*a*c))/2/a
        return r1, r2

print('The equation : a * x^2 + b * x + c = 0')
a=int(input("Please input a: "))
b=int(input("Please input b: "))
c=int(input("Please input c: "))

x1, x2 = quadratic(a,b,c)
print("The solution of this equation are (%s, %s)." % (x1, x2))
