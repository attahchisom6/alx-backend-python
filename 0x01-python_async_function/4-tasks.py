#!/usr/bin/env python3
"""
implementing a a new form of wait_n, in this case, task_wait_random
is being called
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10):
    """
    altering wait_n function
    """
    delay_list = []
    task = task_wait_random(max_delay)
