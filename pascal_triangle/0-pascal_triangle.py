#!/usr/bin/python3
"""
This function looks to return a set a numbers that represent the Pascal Triangle
"""
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        level = [1] + [triangle[i - 1][j] + triangle[i - 1][j + 1] for j in range(i - 1)] + [1]
        triangle.append(level)

    return triangle

