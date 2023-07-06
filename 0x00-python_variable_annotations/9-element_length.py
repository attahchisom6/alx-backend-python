#!/usr/bin/env python3
"""
Annontating a sample function
"""
from typing import List, Tuple, Sequence, Iterable, Iterable


def element_length(lst: Iterable[Sequene]) -> List[Tuple[Sequence, int]]:
    """annotating for sequence of iterables
    """
    return [(i, len(i)) for i in lst]
