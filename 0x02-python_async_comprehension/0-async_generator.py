#!/usr/bin/env python3
"""
A coeoutine with generated using async generator
"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    this coroutine will loop ten times then, each time asynchronously wait 1
    second then yeld a random number between 0 and 10
    """
    def rand() -> float:
        """
        return random float value from 0 to 10
        """
        return random.uniform(0, 10)
    for _ in range(10):
        await asyncio.sleep(1)
        yield rand()
