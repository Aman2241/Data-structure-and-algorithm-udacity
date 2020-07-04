import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
        ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None

    min = ints[0]
    max = ints[0]

    for num in ints:
        if num < min:
            min = num
        if num > max:
            max = num

    return (min, max)

# ----------------------------------------------------------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------------------------------------------------------

# Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

assert((0, 9) == get_min_max(l))

# Test Empty List
assert(get_min_max([]) is None)

# Test Repeating Numbers
assert((0, 0) == get_min_max([0, 0, 0, 0, 0, 0, 0, 0]))
