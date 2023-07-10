#!/usr/bin/env python3
"""
A non Async function returninh asyn task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    task an integer and returns async object 'asyncio.Task
    """
    async def inner():
        """
        needs an async function to inorser to await for a proper task
        """
        await wait_random(max_delay)

    loop = asyncio.get_event_loop()
    task = asyncio.create_task(inner())
    return task
