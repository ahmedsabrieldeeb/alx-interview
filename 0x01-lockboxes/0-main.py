#!/usr/bin/env python3
"""
0-main
"""

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1, 100], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4, 100], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

boxes = []
for i in range(1000):
    boxes.append(list(range(1000)))
print(canUnlockAll(boxes))