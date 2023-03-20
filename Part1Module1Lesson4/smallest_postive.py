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
