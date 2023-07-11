#!/usr/bin/env python3
"""
A coroutine rhat defines async comprehension
"""
import asyncio
from typing import Generator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[List[float], None, None]:
    """
    This coroutine will collect 10 random numbers using async comprehension
    over the coroutine async generator then return the 10 random numbers
    """
    ten_rand_list = [k async for k in async_generator()]
    return ten_rand_list
