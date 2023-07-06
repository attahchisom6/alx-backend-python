#!/usr/bin/env python3
"""
Adding type Annotations based only on given parameters and return value
"""
from typing import Mapping, Union, Any


def safely_get_value(dct: Mapping, key: Any, default: Union[Any, None] = None) -> Union[Any, None]:
    """
    Annontating value returned by dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
