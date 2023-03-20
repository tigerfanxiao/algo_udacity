# Define a control structure that finds the smallest positive
from typing import List


def smallest_positive(in_list:List[float]):
    if len(in_list) == 0:
        return None
    smallest = in_list[0]
    for number in in_list:
        if smallest > number >= 0:
            smallest = number
    if smallest < 0:
        return None
    return smallest


# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

print(smallest_positive([-6, -9, -7]))
# Correct output: None

print(smallest_positive([]))
# Correct output: None