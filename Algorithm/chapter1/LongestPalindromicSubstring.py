# -*- coding: utf-8 -*-

# O(n^3)的枚举法解决最长回文子串（Longest Palindromic Substring）

def longestPalindrome(s):
    longest = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if isPalindrome(s, i, j):
                longest = max(longest, j-i+1)
    return longest
                
def isPalindrome(s, left, right):
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True