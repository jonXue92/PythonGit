# -*- coding: utf-8 -*-

from collections import deque

queue = deque()
seen = set()

seen.add(start)
queue.append(start)
queue.append(None)
currentLevel = 0
while len(queue) > 1:
    head = queue.popleft()
    if head == None:
        currentLevel += 1
        queue.append(None)
        continue
    for neighbor in head.neighbors:
        if neighbor not in seen:
            seen.add(neighbor)
            queue.append(neighbor)