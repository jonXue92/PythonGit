# -*- coding: utf-8 -*-

from printTree import print_tree

# 为了和编码对应，增加一个无用的0在首位
origin = [0, 30, 20, 80, 40, 50, 10, 60, 70, 90]
total = len(origin) - 1  # 初始待排序元素个数，即n
print(origin)
print_tree(origin)
print("="*50)
def heap_adjust(n, i, array: list):
    '''
    调整当前结点(核心算法)
    调整的结点的起点在n//2，保证所有调整的结点都有孩子结点
    :param n: 待比较数个数
    :param i: 当前结点的下标
    :param array: 待排序数据
    :return: None
    '''
    while 2 * i <= n:
        # 孩子结点判断 2i为左孩子，2i+1为右孩子
        lchile_index = 2 * i
        max_child_index = lchile_index  # n=2i
        if n > lchile_index and array[lchile_index + 1] > array[lchile_index]:  # n>2i说明还有右孩子
            max_child_index = lchile_index + 1  # n=2i+1
        # 和子树的根结点比较
        if array[max_child_index] > array[i]:
            array[i], array[max_child_index] = array[max_child_index], array[i]
            i = max_child_index  # 被交换后，需要判断是否还需要调整
        else:
            break
        # print_tree(array)

# 构建大顶堆、大根堆
def max_heap(total,array:list):
    for i in range(total//2,0,-1):
        heap_adjust(total,i,array)
    return array
print_tree(max_heap(total,origin))
print("="*50)

#排序
def sort(total, array:list):
    while total > 1:
        array[1], array[total] = array[total], array[1] # 堆顶和最后一个结点交换
        total -= 1
        # 如果最后剩余2个元素的时候，如果后一个结点比堆顶大，就不用调整了。
        if total == 2 and array[total] >= array[total-1]:
            break
        heap_adjust(total,1,array)
    return array
print_tree(sort(total,origin))
print(origin)