#!/usr/bin/env python3
"""
Adding type Annotations based only on given parameters and return value
"""
from typing import Mapping, Union, Any, TypeVar
T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """
    Annontating value returned by dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
