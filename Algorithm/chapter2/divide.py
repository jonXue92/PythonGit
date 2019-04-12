# -*- coding: utf-8 -*-

# 基本思路是利用减法, 看看被除数可以减去多少次除数.
# 使用倍增的思想优化, 可以将减法的次数优化到对数时间复杂度.
# 我们将除数左移一位(或者让它加上自己), 即得到了二倍的除数, 这时一次减法相当于减去了2个除数. 不断倍增, 时间效率很优秀.
# 与此同时还需要一个变量记录此时的除数是最初的除数的多少倍, 每次减法后都加到结果上即可.

class Divide:
    def divide(self, dividend, divisor):
        INT_MAX = 2147483647
        if divisor == 0:
            return INT_MAX
        neg = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
        a, b = abs(dividend), abs(divisor)
        ans, shift = 0, 31
        while shift >= 0:
            if a >= b << shift:
                a -= b << shift
                ans += 1 << shift
            shift -= 1
        if neg:
            ans = 0 - ans
        if ans > INT_MAX:
            return INT_MAX
        return ans