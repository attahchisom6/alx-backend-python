#!/usr/bin/env python3
"""
annotating a function returning list
"""


def sum_list(input_list: list[float]) -> float:
    """
    this function will all entries in the given list A
    and return the sum as a float
    """
    sum: float = 0
    for num in input_list:
        sum += num
    return float(sum)
