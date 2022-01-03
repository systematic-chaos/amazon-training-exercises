'''
Positive Subsequence Sum

Given a list of numbers, compute the sum of the maximum positive sequence, this is, the sum
of the sequence of consecutive non-negative numbers whose addition reaches a maximum value.

Also, given a list of numbers, compute the sum of the longest positive sequence, this is, the sum
of the longest sequence (in terms of number of elements) of consecutive non-negative numbers.
'''

def positive_sequence_max_sum(num_list: list) -> int:
    if all(num < 0 for num in num_list):
        return max(num_list)
    
    max_sum = 0
    current_sum = 0
    for num in num_list:
        if num >= 0:
            current_sum += num
        else:
            max_sum = max(max_sum, current_sum)
            current_sum = 0
    max_sum = max(current_sum, max_sum)
    return max_sum

def longest_positive_sequence_sum(num_list):
    if all(num < 0 for num in num_list):
        return 0
    
    pos_seq_max_len = 0
    current_positive_sequence_length = 0
    for index, num in enumerate(num_list):
        if num >= 0:
            current_positive_sequence_length += 1
        else:
            if current_positive_sequence_length > pos_seq_max_len:
                pos_seq_max_len = current_positive_sequence_length
                positive_sequence_end_index = index
            current_positive_sequence_length = 0
    
    if current_positive_sequence_length > pos_seq_max_len:
        pos_seq_max_len = current_positive_sequence_length
        positive_sequence_end_index = index
    return sum(num_list[(positive_sequence_end_index - pos_seq_max_len) : positive_sequence_end_index])

def validate_test_suite(test_suite: list, results: list, solutions: list):
    for case, result, solution in zip(test_suite, results, solutions):
        validate_test_case(case, result, solution)

def validate_test_case(test_input: list, result: int, solution: int):
    print('Input:', test_input)
    print('Result:', result)
    print('Result {}matches solution: {}\n'\
        .format('' if result == solution else 'NOT ', solution))

    


test_cases = [ [-1, 0, 7, -3, 100, -1000],
                [6, 2, 0, 1, -3, -1, -7, 5, -10],
                [-100, -5, -1000, -200],
                [5, -1000, -100, 200, 104, 3, -1000, -895] ]

# Test case 1: positive sequence max sum
print('Positive sequence max sum\n')
expected_result = [100, 9, -5, 307]
my_results = [ positive_sequence_max_sum(test_list) for test_list in test_cases ]
validate_test_suite(test_cases, my_results, expected_result)

# Test case 2: longest positive sequence sum
print('\n\n\nLongest positive sequence sum\n')
expected_result = [7, 9, 0, 307]
my_results = [ longest_positive_sequence_sum(test_list) for test_list in test_cases ]
validate_test_suite(test_cases, my_results, expected_result)
