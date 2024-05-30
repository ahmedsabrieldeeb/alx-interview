#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n: int) -> list[list[int]]:
    """
    Generate Pascal's triangle up to a given number of rows.

    Args:
    n (int): The number of rows to generate in the triangle.

    Returns:
    pascal list[list[int]]: A list of lists representing Pascal's triangle.
    """

    if (n <= 0):
        return []

    pascal = []
    pascal.append([1])

    for i in range(1, n):
        rowList = [1]*(i+1)

        for j in range(1, i):
            rowList[j] = pascal[i-1][j-1] + pascal[i-1][j]

        pascal.append(rowList)

    return pascal
