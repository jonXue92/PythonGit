# -*- coding: utf-8 -*-

from input import get_sort_data


def print_data(sort_data, heap_size):
    """
    输出当前数据排序结果
    :param sort_data:
    :param heap_size:
    :return:
    """
    i = 0
    print("heap_size：", heap_size,)
    print("[",)
    while i < heap_size:
        print(sort_data[i],)
        i += 1
    print("](",)
    while i < len(sort_data):
        print(sort_data[i],)
        i += 1
    print(")")


def exchange(sort_data, i, j):
    """
    交换数组中 i, j 下标的两个元素
    :param sort_data:
    :param i:
    :param j:
    :return:
    """
    sort_data[i], sort_data[j] = sort_data[j], sort_data[i]


def heap_sort(sort_data):
    build_max_heap(sort_data)                   # 构建最大堆
    heap_size = len(sort_data)                  # 初始 heap_size 是数组大小，即所有元素都在堆中
    while heap_size > 1:
        print_data(sort_data, heap_size)
        exchange(sort_data, heap_size - 1, 0)   # 把堆顶 最大的元素放到堆尾部。（说明：该元素是大小为 heap_size 的堆中最大的元素，大数放在尾部）
        heap_size -= 1                          # 上一步移出了堆的最大元素，堆的大小减一，
        max_heapify(sort_data, heap_size, 0)    # 由于把尾部的元素放到了堆顶，则对堆顶（下标为0）调用 max_heapify，维护最大堆的性质


def build_max_heap(sort_data):
    """
    构造最大堆：
    只需要倒叙遍历 非叶子节点，维护最大堆的性质，即可保证生成最大堆
    :param sort_data:
    :return:
    """
    half_index = range(0, len(sort_data) / 2)
    half_index.reverse()
    heap_size = len(sort_data)
    for i in half_index:
        max_heapify(sort_data, heap_size, i)


def max_heapify(sort_data, heap_size, i):
    """
    分别比较左右子节点，找出最大节点
    如果最大节点不是 i，则与 i 交换位置，并使用交换位置的下标，递归调用 max_heapify，保证下面的元素维持最大堆的性质
    否则，不用做任何操作
    :param sort_data:
    :param heap_size:
    :param i:
    :return:
    """
    left = i * 2 + 1
    right = (i + 1) * 2
    max_index = i
    if left < heap_size and sort_data[left] > i:
        max_index = left
    if right < heap_size and sort_data[right] > sort_data[max_index]:
        max_index = right
    if max_index != i:
        exchange(sort_data, i, max_index)
        max_heapify(sort_data, heap_size, max_index)


def main():
    sort_data = get_sort_data()
    print("原始数据：", sort_data)
    heap_sort(sort_data)
    print(sort_data)


if __name__ == '__main__':
    main()