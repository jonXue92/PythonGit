# -*- coding: utf-8 -*-

class LongestPalindromeDp:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome_dp(self, s):
        if not s:
            return ""
        
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        
        for i in range(n):
            is_palindrome[i][i] = True
        for i in range(1, n):
            is_palindrome[i][i - 1] = True
            
        longest, start, end = 1, 0, 0
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                is_palindrome[i][j] = s[i] == s[j] and is_palindrome[i + 1][j - 1]
                if is_palindrome[i][j] and length > longest:
                    longest = length
                    start, end = i, j
                    
        return s[start:end + 1]