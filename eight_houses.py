'''
Eight Houses

Eight houses, represented as cells, are arranged in a straight line. Each day every cell
competes with its adjacent cells (neighbors). An integer value of 1 represents an active cell
and a value of 0 represents an inactive cell. If the neighbors on both sides of a cell are
either active or inactive, the cell becomes inactive on the next day; otherwise the cell becomes
active. The two cells on each end have a single adjacent cell, so assume that the unoccupied
space on the opposite side is an inactive cell. Even after updating the cell state, consider its
previous state when updating the state of other cells. The state information of all cells should
be updated simultaneously.

Algorithm that outputs the state of the cells after the given number of days.

Input:
The input to the function consists of two arguments:
`states`, a list of integers representing the current state of cells;
`days`, an integer representing the number of days.

Output:
Return a list of integers representing the state of the cells after the given number of days.

Note:
The elements of the list `states` contains 0s and and 1s only.
'''

from __future__ import annotations

# Return the state in all cells within a given period of days
def cell_compete(states: list, days: int) -> list:
    for _ in range(days):
        states = [ next_day_state(states, i) for i in range(len(states)) ]
    return states

# Return the state of the cell in index for the next day
def next_day_state(cells: list, index: int) -> int:
    if index == 0:  # first cell
        next_state = cells[1] == 1
    elif index == len(cells) - 1:   # last cell
        next_state = cells[len(cells) - 1] == 1
    else:
        next_state = cells[index - 1] != cells[index + 1]
    # Codify boolean result into an integer
    return 1 if next_state else 0

def validate_test_case(test_input: tuple[list, int], result: list, solution: list):
    print('Input:', test_input)
    print('Result:', result)
    print('Result {}matches solution: {}\n'\
        .format('' if result == solution else 'NOT ', solution))




# Test cases evaluation

test_states = [ ([0, 1, 1, 1, 0, 1, 0, 1], 2),
                ([1, 1, 0, 1, 0, 0, 0, 1], 6) ]
test_results = [ [1, 1, 0, 0, 1, 0, 1, 1],
                [1, 1, 0, 1, 1, 0, 1, 1] ]

for case, solution in zip(test_states, test_results):
    my_result = cell_compete(case[0], case[1])
    validate_test_case(case, my_result, solution)
