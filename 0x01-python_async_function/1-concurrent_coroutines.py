#!/usr/bin/env python3
"""
getting a randtime a max number of times
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    An asyn routine that spawns wait_random n times, with the specified
    max delay
    """
    delay_list = []
    done_spawned = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        done_spawned.append(task)

    # Here we will get the values as they are completed, so as to get
    # an ordered list in ascending order
    for spawned in asyncio.as_completed(done_spawn):
        completed = await spawned
        delay_list.append(completed)
    return delay_list
