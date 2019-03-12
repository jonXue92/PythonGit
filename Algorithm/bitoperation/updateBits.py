# -*- coding: utf-8 -*-

class UpdateBits:
    def updateBits(self, n, m, i, j):
        tmp = ((~((((-1) << (31 - j) & 0xFFFFFFFF) >> (31 - j + i)) << i)) & 0xFFFFFFFF) & n | ((m << i) & 0xFFFFFFFF)
        if tmp & (1 << 31):
            return tmp ^ ~(0xFFFFFFFF)
        return tmp