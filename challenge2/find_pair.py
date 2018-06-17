#!/usr/bin/env python3

import os
import sys
from collections import namedtuple

def parse_lines(file_path):
    '''
    Return a list of objects containing the item name and prices from
    the lines in the input file
    '''

    Gift = namedtuple('Gift', ['item', 'price'])
    gifts = []
    with open(file_path) as f:
        for line in f:
            item, price = line.split(',')
            gifts.append(Gift(item, int(price.strip())))

    return gifts


def pick_best(gifts, target):
    '''
    Return the best pair of items minimally under a target
    from from a list of items and prices

    Iterating the left pointer forward and the right pointer backward,
    we keep track of the best two values that sum less than or equal to the target.
    '''

    current_diff, min_diff = None, None
    best_gifts = (None, None)
    l_ptr, r_ptr = 0, len(gifts) - 1

    while l_ptr < r_ptr:
        current_diff = target - (gifts[l_ptr].price + gifts[r_ptr].price)

        # If we find the pair that sum to the target return
        if current_diff == 0:
            return (gifts[l_ptr], gifts[r_ptr])

        if current_diff < 0:
            r_ptr -= 1
        else:
            # If a smaller difference is found, update the min_diff and the best pair
            if min_diff is None or current_diff < min_diff:
                min_diff = current_diff
                best_gifts = (gifts[l_ptr], gifts[r_ptr])

            l_ptr += 1     

    # If no good values are found return (None, None)
    return best_gifts


if __name__ == '__main__':
    if not len(sys.argv) == 3:
        print('ERROR: The command line must have two inputs')
        sys.exit(1)

    # Get the inputs from the command line
    _, PRICES_FILE, TARGET = sys.argv

    if not os.path.isfile(PRICES_FILE):
        print('ERROR: The first command line input must be a valid file')
        sys.exit(1)

    if not TARGET.isdigit():
        print('ERROR: The second command line input must be a valid integer')
        sys.exit(1)

    # Parse the file and return a list of items and prices
    gifts = parse_lines(PRICES_FILE)
    # Pick the best pair
    best_gifts = pick_best(gifts, int(TARGET))
    if best_gifts == (None, None):
        print('Not possible')
        sys.exit(0)
    else:
        best_items_price = ', '.join([
            ' '.join([gift.item, str(gift.price)]) for gift in best_gifts
        ])
        print(best_items_price)
        sys.exit(1)
