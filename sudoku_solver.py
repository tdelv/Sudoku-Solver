import copy

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        # Create grid of possible values for each position
        possibilities = []
        for row in board:
            possibilities.append([])
            for col in row:
                if col == '.':
                    possibilities[-1].append(list(map(str, range(1, 10))))
                else:
                    possibilities[-1].append([col])
            
        # Get solution
        solve = self.solvePossibilities(possibilities)
        if solve:
            for row in range(9):
                for col in range(9):
                    board[row][col] = solve[row][col][0]
        else:
            print("Couldn't solve")
            
            
    def solvePossibilities(self, possibilities):
        """
        :type possibilities: List[List[List[str]]]
        :rtype: List[List[List[str]]]? (or None)
        """
        
        # Lists containing each corresponding group of possibility lists
        rows = list(possibilities)
        cols = [[possibilities[row][col] for row in range(9)] for col in range(9)]
        squares = [[possibilities[3*pos[0] + i][3*pos[1] + j] 
                    for i in range(3) for j in range(3)] 
                   for pos in [(i, j) 
                               for i in range(3) for j in range(3)]]
            
        def attack(group):
            """
            :type group: List[List[List[str]]]
            :rtype: bool (did it make a change?)
            """
            ret = False
            for section in group:
                # Look for solved boxes
                for i in range(9):
                    if len(section[i]) == 1:
                        # If solved, kill solved value in rest of group section
                        kill = section[i][0]
                        for j in list(range(i)) + list(range(i + 1, 9)):
                            if kill in section[j]:
                                section[j].remove(kill)
                                ret = True
            
            return ret
            
        # Keep killing until no more changes
        while True:
            if not(any(list(map(attack, [rows, cols, squares])))):
                break
                
        # If empty box, then no solution
        for row in range(9):
            for col in range(9):
                if len(possibilities[row][col]) == 0:
                    return None
               
        # If all boxes are solved, return
        for row in range(9):
            for col in range(9):
                if len(possibilities[row][col]) != 1:
                    break
            else:
                continue
            break
        else:
            return possibilities
        
        # Find first unsolved box, and iterate through possibilities,
        # recurring on each until one leads to a solution
        for p in possibilities[row][col]:
            new_possibilities = copy.deepcopy(possibilities)
            new_possibilities[row][col] = [p]
            solve = self.solvePossibilities(new_possibilities)
            if solve:
                return solve
        
        # If none of these leads to a solution, no solution possible
        return None
