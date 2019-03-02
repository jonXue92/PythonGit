# -*- coding: utf-8 -*-

from collections import deque

def heap_sort(L):
    L_length = len(L) - 1 #引入了一个辅助空间

    first_sort_count = L_length // 2
    for i in range(first_sort_count): #把序列调整为一个大根堆
        heap_adjust(L, first_sort_count - i, L_length)

    for i in range(L_length - 1): # 把堆顶元素和堆末尾的元素交换，然后把剩下的元素调整为一个大根堆
        L = swap_param(L, 1, L_length - i)
        heap_adjust(L, 1, L_length - i - 1)

    return [L[i] for i in range(1, len(L))]

def swap_param(L, i, j):
    L[i], L[j] = L[j], L[i]
    return L

def heap_adjust(L, start, end):
    temp = L[start]

    i = start
    j = 2 * i

    while j <= end:
        if (j < end) and (L[j] < L[j + 1]):
            j += 1
        if temp < L[j]:
            L[i] = L[j]
            i = j
            j = 2 * i
        else:
            break
    L[i] = temp

def main():
    L = deque([50, 16, 30, 10, 60,  90,  2, 80, 70])
    L.appendleft(0)
    print(heap_sort(L))
    
if __name__ == '__main__':
    main()