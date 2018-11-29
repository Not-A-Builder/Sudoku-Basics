"""
This program is using 3 reference lists to predict the numbers that can be placed in Sudoku.
As it is choosing a number randomly, sometimes there will be no possible numbers to fill a certain index.
So, this method is totally junk, as the generated Sudoku will be neither completed nor solvable.
"""

import random

sudokuGrid = [] # the Sudoku
dim = 3 # dimension of a single block
grid_Dim = dim**2 # Sudoku dimension

# INITIALIZING
ref_Row, ref_Column, ref_Block = [], [], []
for i in range(grid_Dim):
    sudokuGrid.append(['N']*grid_Dim)
#    creating the reference lists
    ref_Row.append(list(range(1, grid_Dim + 1)))
    ref_Column.append(list(range(1, grid_Dim + 1)))
    ref_Block.append(list(range(1, grid_Dim + 1)))
    
def merge(R, C, B):
#    returns a list of possible numbers we can put
    poss = []
    for i in range(grid_Dim):
        if R[i] and B[i] and C[i]:
            poss.append(R[i])
    return poss

for j in range(grid_Dim):
    for i in range(grid_Dim):
        k = i//dim + (j//dim)*dim
        poss_List = merge(ref_Row[j], ref_Column[i], ref_Block[k])
        if len(poss_List): # if there is a possibility then place the number
            ind = random.randrange(len(poss_List)) # choosing a random number from the possible list
            sudokuGrid[j][i] = poss_List[ind]
            key = poss_List[ind] - 1
            ref_Row[j][key] = 0
            ref_Column[i][key] = 0
            ref_Block[k][key] = 0
	    
for i in sudokuGrid:
#   prints out the sudokuGrid, but it will not be a Sudoku
    print(*i)
  
