#!/usr/bin/env python3
"""
measuring corourine
"""
import asyncio
from typing import Generator
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> Generator[float, None, None]:
    """
    will the total time elasped in running async_comprehension 4 times
    """
    start = asyncio.get_event_loop().time()
    coroutine = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*coroutine)
    end = asyncio.get_event_loop().time()

    return end - start
