# -*- coding: utf-8 -*-
import sys

class FindPeakII:
    def findPeakII(self, A):
        if not A or not A[0]:
            return None
        return self.find_peak(A, 0, len(A) - 1, 0, len(A[0]) - 1)
    
    def find_peak(self, matrix, top, bottom, left, right):
        if top + 1 >= bottom and left + 1 >= right:
            for row in range(top, bottom + 1):
                for col in range(left, right + 1):
                    if self.is_peak(matrix, row, col):
                        return [row, col]
            return [-1, -1]
        
        if bottom - top < right - left:
            col = (left + right) // 2
            row = self.find_col_peak(matrix, col, top, bottom)
            if self.is_peak(matrix, row, col):
                return [row, col]
            if matrix[row][col - 1] > matrix[row][col]:
                return self.find_peak(matrix, top, bottom, left, col)
            return self.find_peak(matrix, top, bottom, col, right)
        
        row = (top + bottom) // 2
        col = self.find_row_peak(matrix, row, left, right)
        if self.is_peak(matrix, row, col):
            return [row, col]
        if matrix[row - 1][col] > matrix[row][col]:
            return self.find_peak(matrix, top, row, left, right)
        return self.find_peak(matrix, row, bottom, left, right)
    
    def is_peak(self, matrix, x, y):
        return matrix[x][y] == max(matrix[x][y], matrix[x - 1][y], 
                     matrix[x + 1][y], matrix[x][y + 1], matrix[x][y - 1])
    def find_row_peak(self, matrix, row, left, right):
        peak_val = -sys.maxsize
        peak = []
        for col in range(left, right + 1):
            if matrix[row][col] > peak_val:
                peak_val = matrix[row][col]
                peak  = col
        return peak
    
    def find_col_peak(self, matrix, col, top, bottom):
        peak_val = -sys.maxsize
        peak = None
        for row in range(top, bottom + 1):
            if matrix[row][col] > peak_val:
                peak_val = matrix[row][col]
                peak = row
        return peak
    
class FindPeakII2:
    def findPeakII2(self, A):
        if len(A) == 0 or len(A[0]) == 0:
            return [-1, -1]
        left, right, up, down = 0, len(A[0]) - 1, 0, len(A) - 1
        while left + 1 < right or up + 1 < down:
            if right - left > down - up:
                col = (left + right) // 2
                row = self.find_col_peak(A, col, up, down)
                if self.is_peak(A, row, col):
                    return [row, col]
                elif A[row][col] < A[row][col - 1]:
                    right = col
                else:
                    left = col
            else:
                row = (up + down) // 2
                col = self.find_row_peak(A, row, left, right)
                if self.is_peak(A, row, col):
                    return [row, col]
                elif A[row][col] < A[row - 1][col]:
                    down = row
                else:
                    up = row
        for row in [left, right]:
            for col in [up, down]:
                if self.is_peak(A, row, col):
                    return [row, col]
                
        return [-1, -1]
    
    def is_peak(self, A, row, col):
        return A[row][col] > max(A[row][col - 1], A[row][col + 1], A[row - 1][col], A[row + 1][col])
    
    def find_col_peak(self, A, col, up, down):
        value = max(A[row][col] for row in range(up, down + 1))
        for row in range(up, down + 1):
            if A[row][col] == value:
                return row
    def find_row_peak(self, A, row, left, right):
        value = max(A[row][col] for col in range(left, right + 1))
        for col in range(left, right + 1):
            if A[row][col] == value:
                return col