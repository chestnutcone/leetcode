# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 22:23:52 2019

@author: Oliver
"""

"""
You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.

Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Input: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
"""
from pprint import pprint

def updateBoard(board, click):
    row, col = click[0], click[1]
    if board[row][col] == 'M':
        board[row][col] = 'X'
    elif board[row][col] == 'E':       
        row_min, row_max = max(0,row-1), min(row+2, len(board))
        col_min, col_max = max(0,col-1), min(col+2, len(board[row]))
        
        total_mines = len([x for y in board[row_min:row_max] for x in y[col_min:col_max] if x == "M"])

        if total_mines:
            board[row][col] = str(total_mines)
        else:
            board[row][col] = 'B'

            # all adjacent squre shoudl be unveiled recursively
            for i in range(row_min, row_max):
                for j in range(col_min, col_max):
                    if board[i][j] == 'E':
                        board = updateBoard(board, [i,j])
    return board

test_case =[['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'],['B', 'B', 'B', 'B', 'B']]
test_click = [3,0]

test_case =[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

pprint(test_case)
new_board = updateBoard(test_case, test_click)
pprint(new_board)