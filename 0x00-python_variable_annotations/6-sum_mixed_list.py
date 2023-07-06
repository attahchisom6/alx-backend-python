#!/usr/bin/env python3
"""
Annontating mixed values
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """funcrion to get annotation of the sum of mixed list"""
    sum: float = 0
    for num in mxd_lst:
        sum += num
    return float(sum)
