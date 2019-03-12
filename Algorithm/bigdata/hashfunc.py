# -*- coding: utf-8 -*-

class HashFunction:
    def hashfunc(string, hashsize):
        code = 0
        for c in string:
            code = code * 31 + ord(c)
            code = code % hashsize
            
        return code