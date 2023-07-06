#!/usr/bin/env python3
"""
annotating a function returning list
"""


def sum_list(A: list[float]) -> float:
    """
    this function will all entries in the given list A
    and return the sum as a float
    """
    sum: float = 0
    for num in A:
        sum += num
    return float(sum)
