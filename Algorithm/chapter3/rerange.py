# -*- coding: utf-8 -*-

class Rerange:
    def rerange(self, A):
        if not A or len(A) < 3:
            return A
        left, right = 0, len(A) - 1
        while left <= right:
            while left <= right and A[left] < 0:
                left += 1
            while left <= right and A[right] > 0:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        if 2 * left <= len(A):
            first, second = 0, 2 * left - 1
        else:
            first, second = 1, len(A) - 1
        while first <= second:
            A[first], A[second] = A[second], A[left]
            first += 2
            second += 2
        return A