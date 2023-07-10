#!/usr/bin/env python3
"""
implementing programs that wait for certain criteria before execution
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    this routine neasures the total time taken for each task to be completed
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    tot = time.perf_counter() - start
    return tot / n
