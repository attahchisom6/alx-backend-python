#!/usr/bin/env python3
"""
Annontate a function that returns a function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make or produces a function that multiplies a float by a multilier
    """
    def func(num: float) -> float:
        return multiplier * num
    return func
