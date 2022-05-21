#!/usr/bin/python3
'''
pascals triangle
'''


def pascal_triangle(n):
    '''the triangle method with a nested loop
        function returns lists of lists of int
        but defining the rows utilizing the range()
        function. defining range(n); 
        n being the integer
    '''
    rows = [[1 for xyz in range(qrs + 1)] for qrs in range(n)]
    ''' nested loop that prints the triangle'''
    for n in range(n):
        for qrs in range(n - 1):
            rows[n][qrs + 1] = sum(rows[n - 1][qrs:qrs + 2])
    '''returning the rows that print the numbers of pascals triangle'''
    return rows
