'''
Building Lot

You are in charge of preparing a recently purchased lot for one of Amazon's new buildings.
The lot is covered with trenches and has a single obstacle that needs to be taken down before
the foundation can be prepared for the building. The demolition robot must remove the obstacle
before process can be made on the building.

Algorithm to determine the minimum distance required for the demolition robot
to remove the obstacle.

Assumptions:
* The lot is flat, excepts for trenches, and can be represented as a two-dimensional grid.
* The deomolition robot must start from the top-left corner of the lot, which is always flat,
  and can move one block up, down, left, or right at a time.
* The demolition robot cannot enter trenches and cannot leave the lot.
* The flat areas are represented as 1, areas with trenches are represented by 0 and the
  obstacle is represented by 9.

Input:
The input to the function consists of three arguments:
`numRows`, an integer representing the number of rows;
`numColumns`, an integer representing the number of columns;
`lot`, representing the two-dimensional grid of integers.

Output:
Return an integer representing the minimum distance traversed to remove the obstacle;
else return -1.

Constraints:
1 <= numRows
numColumns <= 1000
'''

from __future__ import annotations
from math import isinf

# Explore the lot by applying dynamic programming techniques
def dynamic_route_expansion(lot: list, current_pos: tuple[int, int], current_cost: int, min_cost: int) -> int:
    if lot[current_pos[0]][current_pos[1]] == 9:    # base case
        return current_cost
    
    # Disable current cell, so that the algorithm will not step back
    lot[current_pos[0]][current_pos[1]] = -1

    # Recursively explore available cells
    for cell in next_available_cells(current_pos, lot):
        aux_cost = dynamic_route_expansion(lot, cell, current_cost + 1, min_cost)
        # if achieved a lower cost, update the minimum cost value
        min_cost = min(min_cost, aux_cost)
    
    # Undo the current cell disablement
    lot[current_pos[0]][current_pos[1]] = 1

    return min_cost

# Return the cells available for going to from the current position
def next_available_cells(current_position, lot):
    cells = []

    # Valid cells based on lot borders
    if current_position[0] > 0:
        cells.append((current_position[0] - 1, current_position[1]))
    if current_position[0] < len(lot) - 1:
        cells.append((current_position[0] + 1, current_position[1]))
    if current_position[1] > 0:
        cells.append((current_position[0], current_position[1] - 1))
    if current_position[1] < len(lot[0]) - 1:
        cells.append((current_position[0], current_position[1] + 1))
    
    # Discard trenches and invalid cells
    return [ c for c in cells if lot[c[0]][c[1]] > 0 ]

def amazon_automata(num_rows: int, num_columns: int, lot: list) -> int:
    if num_rows == 0 or num_columns == 0:
        return -1
    
    min_cost = dynamic_route_expansion(lot, (0, 0), 0, float("inf"))
    return min_cost if not isinf(min_cost) else -1

def validate_test_case(test_input: list, result: int, solution: int):
    print('Input:', test_input)
    print('Result:', result)
    print('Result {}matches solution: {}\n'\
        .format('' if result == solution else 'NOT ', solution))




# Test cases evaluation

test_cases = [ [[1, 0, 0], [1, 0, 0]],
                [[1, 1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 9]],
                [[1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 0, 9]] ]
test_results = [-1, 8, 8]

for case, solution in zip(test_cases, test_results):
    my_result = amazon_automata(len(case), len(case[0]), case)
    validate_test_case(case, my_result, solution)
