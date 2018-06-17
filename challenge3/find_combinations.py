#!/usr/bin/env python3

import sys
from itertools import product


def get_combinations(pattern):
    '''
    Return a combination of all numbers in the pattern with X's replaced with 0s and 1s

    We use a recursive approach to get the combinations of the first element in the array
    with the rest of the elements
    '''

    if len(pattern) == 1:
        if pattern[0] == 'X':
            return ['0', '1']

        return [pattern[0]]

    all_patterns = []
    first_part = get_combinations(pattern[0])
    rest_part = get_combinations(pattern[1:])

    for first, rest in product(first_part, rest_part):
        all_patterns.append(first + rest)

    return all_patterns

if __name__ == '__main__':
    if not len(sys.argv) == 2:
        print('ERROR: The command line must have one input')
        sys.exit(1)

    # Get the inputs from the command line
    _, PATTERN = sys.argv
    # Check if the PATTERN argument is correct
    if set(PATTERN) - set(['0', '1', 'X']):
        print('ERROR: The pattern can only contain 0, 1 and X')
        sys.exit(1)  

    # Find all combinations for X replacement in the string
    combinations = get_combinations(PATTERN)
    for combination in combinations:
        print(combination)
