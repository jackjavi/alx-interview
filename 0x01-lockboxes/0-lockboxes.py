#!/usr/bin/env python3
'''
Module for lockboxes.
'''


def canUnlockAll(boxes):
    '''
    Determines if all boxes can be opened.
    '''
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True

    stack = [0]

    while stack:
        current = stack.pop()
        for key in boxes[current]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
