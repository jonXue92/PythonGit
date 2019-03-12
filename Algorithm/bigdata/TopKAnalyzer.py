# -*- coding: utf-8 -*-

class TopAnalyzer:
    # 构造函数，初始化一个top k 分析器，指定k 的大小
    def __init__(self, k):
        self.k = k
        
        # 初始化一个哈希堆(HashHeap)。这个数据结构是在堆的基础上加一个哈希表。
        # HeahHeap 除了有堆的功能以外，还能查询某个单词是否在这个堆里。
        # 正如标准离线算法一样，这是一个最小堆
        self.hashheap = HashHeap()
        
        # 初始化一个哈希表，用于对单词计数
        self.hash = Hash()
        
    def add(word):
        # 单词计数 +1
        self.hash[word] += 1
        
        if word in self.hashheap:
            # 调整 word 在 hashheap 中的位置，因为它的计数被更改了
            self.hashheap.adjust(word, self.hash[word])
            return
        
        # 如果没满，就接着往hashheap里放：
        if self.hashheap.size() < self.k:
            self.hashheap.push(word, self.hash[word])
            return
        
        # 和 hashheap 里出现频次最低的单词相比
        # 如果当前单词更大，就踢掉hashheap 里的频次最低的单词
        if self.hash[word] > self.hashheap.top().value:
            self.hashheap.pop()
            self.hashheap.push(word, self.hash[word])
            
    def topk():
        # 从hashheap中导出Top k 的单词
        return self.hashheap.toList()