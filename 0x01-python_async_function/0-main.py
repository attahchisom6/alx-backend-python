#!/usr/bin/env python3
"""
test out a code
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random
print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(12)))
