#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    # Write your code here
    n, m = len(grid), len(grid[0])
    count=0
    
    for i in range(n):
        for j in range(m):
            is_dominant = True
            
            for x in range(max(0, i-1), min(n, i+2)):
                for y in range(max(0, j-1), min(m, j+2)):
                    if grid[x][y] >= grid[i][j] and (x, y) != (i, j):
                        is_dominant = False
                        
            if is_dominant:
                count += 1
    return count
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    grid_rows = int(input().strip())
    grid_columns = int(input().strip())
    
    grid = []
    
    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))
        
    result = numCells(grid)
        
    fptr.write(str(result) + '\n')
        
    fptr.close()
