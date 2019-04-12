# -*- coding: utf-8 -*-
class LongestPalindrome:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return ""
        max_length = 0
        result_left, result_right = 0, 0
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left + 1 > max_length:
                        max_length = right - left + 1
                        result_left, result_right = left, right
                    left -= 1
                    right += 1
                else:
                    break
        for i in range(1, len(s)):
            left, right = i - 1, i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left + 1 > max_length:
                        max_length = right - left + 1
                        result_left, result_right = left, right
                    left -= 1
                    right += 1
                else:
                    break
        return s[result_left:result_right + 1]
