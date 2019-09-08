# Sudoku-Solver
A Sudoku Solver written in Python

## Credit
Stencil code from leetcode.com (none of logic)

## To run
Create a `Solution` instance with `Solution()`, and call it's `solveSudoku` method with the board as the parameter. The board should be a List of Lists of strings, with empty spots being `'.'`. The solver will update board in place, so nothing is returned.

## To Do
- Reduce repeated/unnecessary computation by remembering when a given number has been killed in a given section.
