def find_next_empty(puzzle):
    # finds next row, column on the puzzle that's not filled yet -> represented with -1
    # return row, column tuple (or (None, None) if there is none.)
    
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    
    return None, None # if no empty spots in the board

def is_valid(puzzle, guess, row, col):
    # figures out if the guess at the row/column of the puzzle is a valid guess
    # returns True if it is valid, otherwise False
    
    # for a row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # for a column
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
    if guess in col_vals:
        return False
    
    # for the square: we want to get where the 3*3 square starts
    # and iterate over the 3 values in the row/column
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    return True
    
def solve_sudoku(puzzle):
    # solve sudoku using a backtracking technique
    # the puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution
    
    # step 1: choose somehwere on the puzzle to make a guess
    row, col = find_next_empty(puzzle) # use a helper function to find a next empty spot 
    
    # step 1.1: if there's nowhere left on the board, then we're done because only valid inputs were allowed
    if row is None:
        return True # we only need to chek either row or column
    
    # step 2: if there is a place to put a number, then make a guess between 1-9
    for guess in range(1, 10): # the range is 1,2,3.....9
        #step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, then place that guess on the puzzle
            puzzle[row][col] = guess
            # now recurse using this function
            # step 4: recursively call out function
            if solve_sudoku(puzzle):
                return True
        
        #step 5: if not valid, or if the guess does not solve the puzzle, we need to backtrack and try new num
        puzzle[row][col] = -1 #reset the guess
        
    # step 6: if none of the numbers that we try work, then the puzzle is unsolvable
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,     -1, 5, -1,       -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,      -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,        -1, 8, -1],
                     
        [-1, 5, -1,    -1, 6, 8,       -1, -1, -1],
        [2, -1, 6,     -1, -1, 3,      -1, -1, -1],
        [-1, -1, -1,    -1, -1, -1,     -1, -1, 4],      
                     
        [5, -1, -1,    -1, -1, -1,     -1, -1, -1],
        [6, 7 , -1,    -1, -1, 5,      -1, 4, -1],
        [1, -1, 9,     -1, -1, -1,     2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)
        