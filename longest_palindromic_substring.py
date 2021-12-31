'''
Longest Palindromic Substring

An O(n^2) time and O(1) space program to find the longest palindromic substring.
'''

from __future__ import annotations

# Solution access-point function
def longest_palindromic_substring(input_string: str) -> tuple[str, int, int]:
    if input_string:
        max_palindrome = input_string[0]
        max_pal_length = 1
        start_index = 0
    else:
        return '', 0, 0
    
    for n in range(1, len(input_string)):
        current_palindrome = expand_from_center(input_string, n)
        if current_palindrome[1] > max_pal_length:
            max_palindrome, max_pal_length, start_index = current_palindrome
    
    return max_palindrome, start_index, start_index + max_pal_length

# Convenience function for expanding a string from a given center index
# looking for palindromic strings, both odd-length and even-length.
def expand_from_center(input_str: str, center: int):
    odd = expand_from_center_odd_even(input_str, center, odd=True)
    even = expand_from_center_odd_even(input_str, center, odd=False)
    return even if even[1] > odd[1] else odd

def expand_from_center_odd_even(input_str: str, center: int, odd: bool) -> tuple[str, int, int]:
    max_pal_length = 1
    start_index = center
    string_length = len(input_str)

    # If looking for odd-length palindromes, find the longest one around (center - 1) and center.
    # If looking for even-length palindromes, find the longest one around center.
    higher_bound = center if odd else center + 1
    lower_bound = center - 1

    while lower_bound >= 0 and higher_bound < string_length\
            and input_str[lower_bound] == input_str[higher_bound]:
        pal_length = higher_bound - lower_bound + 1
        if pal_length > max_pal_length:
            max_pal_length = pal_length
            start_index = lower_bound
        higher_bound += 1
        lower_bound -= 1
    
    return input_str[start_index : (start_index + max_pal_length)], max_pal_length, start_index

def validate_test_case(test_input: str, result: tuple[str, int, int], solution: str):
    (palindrome, pal_start_index, pal_end_index) = result
    print('Longest palindromic substring in {} is {}'.format(test_input, palindrome))
    print('Located within indexes {} and {}'.format(pal_start_index, pal_end_index))
    print('Result {}matches solution: {}\n'\
        .format('' if palindrome == solution else 'NOT ', solution))




# Dummy functional test case
test_string = 'forgeeksskeegfor'
expected_result = 'geeksskeeg'
my_result = longest_palindromic_substring(test_string)
validate_test_case(test_string, my_result, expected_result)
