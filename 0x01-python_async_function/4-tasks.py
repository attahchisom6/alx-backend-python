#!/usr/bin/env python3
"""
implementing a a new form of wait_n, in this case, task_wait_random
is being called
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    altering wait_n function
    """
    delay_list = []
    done_spawned = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        done_spawned.append(task)

    for spawned in asyncio.as_completed(done_spawned):
        completed = await spawned
        delay_list.append(completed)
    return delay_list
