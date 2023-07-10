#!/usr/bin/env python
"""
Creating asynx function ro wait for a max time b4 returning
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
