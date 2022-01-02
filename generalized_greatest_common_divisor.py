'''
Generalized Greatest Common Divisor

Algorithm to determine the GCD of N positive integers.

The greatest common divisor (GCD), also called highest common factor (HCF) of N numbers
is the largest positive integer that divides all numbers without giving a remainder.

The input to the function consists of a single argument `num_list`: a list of positive integers.
It returns an integer representing the GCD of the given positive integers.
'''

# Generalized GCD of the (positive integer) numbers in `num_list`
def generalized_gcd(num_list: list) -> int:
    # Generalized GCD is between 1 and the minimum element of num_list
    gcd = min(num_list)

    # Decrement until a valid generalized GCD is found
    while gcd > 1 and any(n % gcd != 0 for n in num_list):
        gcd -= 1
    return gcd

def validate_test_case(test_input: list, result: int, solution: int):
    print('Input:', test_input)
    print('Result:', result)
    print('Result {}matches solution: {}\n'\
        .format('' if result == solution else 'NOT ', solution))




# Test cases evaluation

test_cases = [ [2, 4, 6, 8, 10, 12],
                [3, 5, 7, 9],
                [5, 10, 20, 25, 50, 100, 200]]
test_results = [2, 1, 5]

for case, solution in zip(test_cases, test_results):
    my_result = generalized_gcd(case)
    validate_test_case(case, my_result, solution)
