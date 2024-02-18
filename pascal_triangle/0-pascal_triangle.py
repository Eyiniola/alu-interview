#!/usr/bin/python3
"""
This function looks to return a set a numbers that represent the Pascal Triangle
"""
def pascal_triangle(n):
    """
    Generates the Pascal's triangle up to level n.

    Args:
        n (int): The number of levels in the Pascal's triangle.

    Returns:
        list: A list of lists representing the Pascal's triangle.
    """

    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first level with 1

    for i in range(1, n):
        # Create the next level by adding the previous level's elements
        # and their neighbors, handling edge cases.
        level = [1] + [triangle[i - 1][j] + triangle[i - 1][j + 1] for j in range(i - 1)] + [1]
        triangle.append(level)

    return triangle

# Example usage
n = 5
triangle = pascal_triangle(n)

for row in triangle:
    print(row)

