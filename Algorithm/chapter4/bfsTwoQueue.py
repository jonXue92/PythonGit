# -*- coding: utf-8 -*-

from collections import deque

# queue1就是保存当前层的节点，queue2就是保存下一层的节点
queue1, queue2 = deque(), deque()
seen = set()

seen.add(start)
queue1.append(start)
currentLevel = 0
while len(queue1):
    size = len(queue1)
    for _ in range(size):
        head = queue1.popleft()
        for neighbor in head.neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
                queue2.append(neighbor)
    queue1, queue2 = queue2, queue1
    queue2.clear()
    currentLevel += 1