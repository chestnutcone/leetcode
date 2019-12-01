# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 22:23:52 2019

@author: Oliver
"""


def solveSudoku(board):
    """
    Do not return anything, modify board in-place instead.
    """

    valid_pos = {0,1,2,3,4,5,6,7,8}
    total_space = {(r,c) for r in range(9) for c in range(9)}
    
    def isValidSudoku(board):
        cols = [[] for _ in range(9)]
        # do row, cols first
        for r in board:
            filtered_ls = [n for n in r if n != "."]
            filtered_set = set(filtered_ls)
            if len(filtered_ls) != len(filtered_set):
                return False
            for i, num in enumerate(r):
                if num != '.':
                    cols[i].append(num)
    
        # do columns
        for c in cols:
            col_set = set(c)
            if len(c) != len(col_set):
                return False
    
        # do boxes
        for i in range(0,9,3):
            for j in range(0,9,3):
                box_nums = [num for box in board[i:i+3] for num in box[j:j+3] if num != '.']
                box_set = set(box_nums)
                if len(box_nums) != len(box_set):
                    return False
        return True
    def binner(num):
        if num in {0,1,2}:
            return {0,1,2}
        elif num in {3,4,5}:
            return {3,4,5}
        else:
            return {6,7,8}
        
    def square_finder(r,c):
        if r<3:
            return c%3
        elif r<6:
            return c%3+3
        else:
            return c%3+6
        

    def possible_pos(board, num, allowed_space):
        # return set of sets (r,c) of allowed places
        appearance = {(r,c) for r in range(9) for c in range(9) if board[r][c] == str(num)}
        old_appearance = appearance.copy()
        valid_row = valid_pos-{pos[0] for pos in old_appearance}
        valid_col = valid_pos-{pos[1] for pos in old_appearance}
        # do box
        for pos in old_appearance:
            box_r = binner(pos[0])
            box_c = binner(pos[1])
            
            box_appearance = {(r,c) for r in box_r for c in box_c}
            appearance.update(box_appearance)

        valid_places = allowed_space - appearance
        allowed_places = valid_places.intersection({(r,c) for r in valid_row for c in valid_col})
        return allowed_places
    
    def solver(board):
        space_occupied = {(r,c) for r in range(9) for c in range(9) if board[r][c] != "."}
        allowed_space = total_space - space_occupied
        p_board = [x[:] for x in board]
        pre_board = [x[:] for x in board]
    
        num_possibles = {num:possible_pos(board, num, allowed_space) for num in range(1,10)}
        counter = 0
        for val in num_possibles.values():
            if val:
                break
            else:
                counter += 1
        if counter == 9:
            return True,board
        
        for num in range(1,10):
            for position in num_possibles[num]:
                try:
                    p_board[position[0]][position[1]].append(num)
                except:
                    p_board[position[0]][position[1]] = [num]
        
        # check uniqe ones in column
        col_replace_ls = []
        for c in range(9):
            col_possible = [p_board[r][c] for r in range(9) if isinstance(p_board[r][c] ,list)]
            col_possible = [x for ls in col_possible for x in ls]
            uniq_col_pos = set(col_possible)
            col_replace = [num for num in uniq_col_pos if col_possible.count(num)==1]
            col_replace_ls.append(col_replace)

        for r in range(9):
            row_possible = [x for x in p_board[r] if isinstance(x,list)]
            row_possible = [x for ls in row_possible for x in ls]
            
            replace_list = []
            # check for unique ones
            uniq_row_pos = set(row_possible)
            for i, num in enumerate(uniq_row_pos):
                if row_possible.count(num) == 1:
                    # if it only occured once in the row
                    replace_list.append(num)
                    
            for c in range(9):
                if isinstance(p_board[r][c],list):
                    if len(p_board[r][c])==1:
                        board[r][c] = str(p_board[r][c][0])
                        
                    for num in replace_list:
                        if num in p_board[r][c]:
                            board[r][c] = str(num)
                            replace_list.remove(num)
                    
                    for num in col_replace_ls[c]:
                        if num in p_board[r][c]:
                            board[r][c] = str(num)
                            col_replace_ls[c].remove(num)

        if pre_board == board:
            return False, p_board

        for row in p_board:
            for c in row:
                if c == ".":
                    # this shouldnt appear, dead end
                    return False, None
        solver(board)

    solver(board)
    status, answer = solver(board)
    
    def test_dummy(queue, board):
        
        current_q = queue.pop()
        p_board = current_q[3]

        dummy_board = [[y if isinstance(y,str) else "." for y in x] for x in p_board]
        dummy_board[current_q[0]][current_q[1]] = str(current_q[2])

        solver(dummy_board)
        status, answer = solver(dummy_board)
        if status and isValidSudoku(dummy_board):
            for i, row_i in enumerate(dummy_board):
                for j, val in enumerate(row_i):
                    board[i][j] = val
            raise

        if answer:
            for r, row in enumerate(answer):
                for c, col in enumerate(row):
                    if isinstance(col, list):
                        for val in col:
                            queue.append((r,c,val,answer))

        test_dummy(queue, board)

    if status is False:
        test_roots = []
        for r, row in enumerate(answer):
            for c, col in enumerate(row):
                if isinstance(col, list):
                    for val in col:
                        test_roots.append((r,c,val,answer))

        # got all the test_roots
        try:
            test_dummy(test_roots, board)
        except Exception as e:
            print(e)
            pass