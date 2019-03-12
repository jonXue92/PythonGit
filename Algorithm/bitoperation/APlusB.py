# -*- coding: utf-8 -*-

class APlusB:
    def aplusb(self, a, b):
        maxUnsignedInt = (1 << 32) - 1
        # 0xFFFFFFFF
        while b != 0:
            _a = (a ^ b) & maxUnsignedInt
            _b = ((a & b) << 1) & maxUnsignedInt
            a = _a
            b = _b
        return a