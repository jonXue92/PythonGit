# -*- coding: utf-8 -*-

def twoSum(numbers, target):
    hash_set = set()
    
    for i in range(len(numbers)):
        if target-numbers[i] in hash_set:
            return (numbers[i], target-numbers[i])
        hash_set.add(numbers[i])

    return None