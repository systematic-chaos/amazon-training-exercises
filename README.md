# Amazon training exercises

**`longest_palindromic_substring.py`:**
An $O(n^{2})$ time and $O(1)$ space program to find the _longest palindromic substring_.

**`generalized_greatest_common_divisor.py`:**
Algorithm to determine the GCD of N positive integers.
The _greatest common divisor_ (GCD), also called highest common factor (HCF) of N numbers is
the largest positive integer that divides all numbers without giving a remainder.

**`positive_subsequence_sum.py`:**
Given a list of numbers, compute the _sum of the maximum positive sequence_, this is, the sum
of the sequence of consecutive non-negative numbers whose addition reaches a maximum value.
Also, given a list of numbers, compute the _sum of the longest positive sequence_, this is, the sum
of the longest sequence (in terms of number of elements) of consecutive non-negative numbers.

**`reverse_nodes_in_k_group.py.py`:**
Given a linked list, _reverse its nodes, `k` at a time_, and return the modified list.
`k` is a positive integer that is less than or equal to the length of the list provided.
If the number of nodes is not a multiple of `k`, then left-out nodes, in the end, should remain as they are.
Values in the list's nodes must not be altered, only nodes references can be changed.

**`eight_houses.py`:**
Eight houses, represented as cells, are arranged in a straight line. Each day every cell
competes with its adjacent cells (neighbors). An integer value of 1 represents an active cell
and a value of 0 represents an inactive cell. If the neighbors on both sides of a cell are
either active or inactive, the cell becomes inactive on the next day; otherwise the cell becomes
active. The two cells on each end have a single adjacent cell, so assume that the unoccupied
space on the opposite side is an inactive cell. Even after updating the cell state, consider its
previous state when updating the state of other cells. The state information of all cells should
be updated simultaneously.

**`alexa_vegetarian_restaurants.py`:**
Amazon's Alexa team is working on optimizing the customer experience for scenarios where
customers ask generic questions. One example of a generic question is "What are good
vegetarian restaurants nearby?". In this scenario, Alexa would then search for a list of
vegetarian restaurants in the city and select the nearest X vegetarian restaurants relative
to the customer's location.
Given an array representing the locations of N vegetarian restaurants in the city,
this algorithm finds the nearest X vegetarian restaurants to the customer's location.
