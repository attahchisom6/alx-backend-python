#!/usr/bin/env python3
"""
Annotating a function using ducked-typed annotation
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    docker-Annoting a function to return either the first element in
    the list or None
    """
    if lst:
        return lst[0]
    else:
        return None
