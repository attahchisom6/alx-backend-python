#!/usr/bin/env python3
"""
Annotating a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """this will take string, float or integer argument and return
    a tuple of string and float data types
    """
    return (k, v * v)
