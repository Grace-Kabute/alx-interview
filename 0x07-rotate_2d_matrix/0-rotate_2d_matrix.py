#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    function rotates 2D matrix by 90 degrees
    """
    n = len(matrix)
    for row in range(0, int(n / 2)):

        for col in range(row, n - row - 1):
            # print((row,col))
            temp = matrix[row][col]

            # print((row,col), (n - 1 - col,row))
            matrix[row][col] = matrix[n - 1 - col][row]

            # print((n - 1 - col,row), (n - 1 - row,n - 1 - col))
            matrix[n - 1 - col][row] = matrix[n - 1 - row][n - 1 - col]

            # print((n - 1 - row,n - 1 - col), (col,n - 1 - row))
            matrix[n - 1 - row][n - 1 - col] = matrix[col][n - 1 - row]

            # print((col,n - 1 - row))
            matrix[col][n - 1 - row] = temp
