# -*- coding: utf-8 -*-

from collections import deque

queue = deque()
# set存储已经访问过的节点（已经丢到 queue 里去过的节点）
seen = set()

seen.add(start)
queue.append(start)
while len(queue):
    head = queue.popleft()
    # neighbor 表示从某个点 head 出发，可以走到的下一层的节点。
    for neighbor in head.neighbors:
        if neighbor not in seen:
            # set与 queue 是一对好基友，无时无刻都一起出现，往 queue 里新增一个节点，就要同时丢到 set 里。
            seen.add(neighbor)
            # queue 存储等待被拓展到下一层的节点
            queue.append(neighbor)
