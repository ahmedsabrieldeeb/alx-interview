#!/usr/bin/python3
"""
This module contains a function to determine if all the boxes
in a given list can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes in the given list can be unlocked.

    Args:
        boxes (list): A list of lists representing the lockboxes.
                      Each inner list contains the keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    # setup the algorithm
    num_boxes = len(boxes)
    visited = [0] * num_boxes
    visited[0] = 1

    # start search
    dfs_traversal(boxes[0], boxes, visited, num_boxes)

    # check whether all nodes visited or not
    if 0 in visited:
        return False
    else:
        return True


def dfs_traversal(box, boxes, visited, num_boxes):
    """
    Perform a depth-first search traversal on a box and its sub-boxes.

    Args:
        box (list): The current box being visited.
        boxes (list): The list of all boxes.
        visited (list): A list to keep track of visited boxes.
        num_boxes (int): The total number of boxes.

    Returns:
        Void: returns nothing
    """
    for key in box:
        # only visit boxes existed and hasn't been visited
        if key < num_boxes and visited[key] == 0:
            visited[key] = 1
            dfs_traversal(boxes[key], boxes, visited, num_boxes)
