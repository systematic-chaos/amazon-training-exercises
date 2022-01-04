'''
Reverse Nodes in a k-Group

Given a linked list, reverse its nodes, `k` at a time, and return the modified list.

`k` is a positive integer that is less than or equal to the length of the list provided.
If the number of nodes is not a multiple of `k`, then left-out nodes, in the end, should remain as they are.

Values in the list's nodes must not be altered, only nodes references can be changed.
'''

from __future__ import annotations
from typing import Optional

def reverse_k_group(head: ListNode, k: int) -> ListNode:
    current_node = ListNode(head.val, None)     # copy first node
    next_node = head.next       # pointer to the next node in the original list
    new_head = current_node     # first node in the reversed list
    previous_group_tail = None

    i = 0
    while next_node is not None:
        if i == 0:      # beginning of node group
            # Keep a reference to the end (after reverse) of the current group.
            current_group_tail = current_node

        if i < k - 1:
            # Create a clone of the next node that points to the current one.
            new_node = ListNode(next_node.val, current_node)
            
        else:       # end of node group
            # The head of the global reversed list is the head of the first group.
            if new_head is current_group_tail:
                new_head = current_node

            # The tail of the current group points by default to the next node in the global list.
            new_node = ListNode(next_node.val, next_node.next)
            current_group_tail.next = next_node

            # Join the tail of the previous group to the head of the current group and keep a
            # reference to the tail of the group just being completed for the next iteration.
            if previous_group_tail is not None:
                previous_group_tail.next = current_node
            previous_group_tail = current_group_tail

        # Traversing to the next node.
        next_node = next_node.next
        current_node = new_node
        i = (i + 1) % k

    return new_head

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def to_array(self) -> list:
        return ListNode.linked_list_to_array(self)
    
    @staticmethod
    def linked_list_to_array(head_node: ListNode) -> list:
        array = []
        current_node = head_node
        while current_node is not None:
            array.append(current_node.val)
            current_node = current_node.next
        return array
    
    @staticmethod
    def linked_list_from_array(array: list) -> Optional[ListNode]:
        next_node = None
        for current_value in reversed(array):
            next_node = ListNode(current_value, next_node)
        return next_node

def validate_test_case(test_input: list, result: ListNode, solution: list):
    result = result.to_array()
    
    print('Input:', test_input)
    print('Result:', result)
    print('Result {}matches solution: {}\n'\
        .format('' if result == solution else 'NOT ', solution))




# Test cases evaluation

test_cases = [ ([1, 2, 3, 4, 5], 2),
                ([1, 2, 3, 4, 5], 3),
                ([1, 2, 3, 4, 5], 1),
                ([1], 1) ]
test_results = [ [2, 1, 4, 3, 5],
                [3, 2, 1, 4, 5],
                [1, 2, 3, 4, 5],
                [1] ]

for case, solution in zip(test_cases, test_results):
    my_result = reverse_k_group(ListNode.linked_list_from_array(case[0]), case[1])
    validate_test_case(case, my_result, solution)
