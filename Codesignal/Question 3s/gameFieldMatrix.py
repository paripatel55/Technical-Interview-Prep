'''
Game Field Matrix Puzzle
You are given a matrix of integers field of size n × m representing a game field, 
and a matrix of integers figure of size 3 × 3 representing a figure. 
Both matrices contain only 0s (free cell) and 1s (occupied cell).

Your task is to drop the figure onto the field from a position at the top such that 
it descends straight down until it reaches the bottom of the field or lands on a c
ell that is occupied. Your goal is to find a dropping position that results in 
at least one fully occupied row. The dropping position corresponds to 
the column index of the cell in the field that aligns with the top-left corner of the figure.

If multiple positions satisfy the condition, any one of them is an acceptable output. 
If no such positions exist, return -1.

Note: The 3 × 3 figure matrix must be entirely inside the game field during the drop, 
even if parts of the figure are unoccupied.

Examples:
For a field:

[[0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [1, 1, 0, 1, 0],
 [1, 0, 1, 0, 1]]
And a figure:

[[1, 1, 1],
 [1, 0, 1],
 [1, 0, 1]]
The output should be findFullLine(field, figure) = 2.

If no fully occupied line can be formed, the output should be findFullLine(field, figure) = -1.

Constraints:
4 ≤ field.length ≤ 100
3 ≤ field[i].length ≤ 100
0 ≤ field[i][j] ≤ 1
The figure's occupied cells are pairwise connected, and there's at least one occupied cell at the figure's bottom row.
Input/Output:
[input] array.array.integer field
A matrix of integers representing the game field.
[input] array.array.integer figure
A matrix of integers representing the figure.
[output] integer
The dropping position such that a full row is formed, any if multiple, -1 if none.
'''