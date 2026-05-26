#!/usr/bin/env python3
""" Programme that executes multiple coroutines at the same time with async """
import asyncio
from 0_basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int = 10) -> list[float]:
    """ Function that returns the list
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
