#!/usr/bin/env python3
""" Let's execute multiple coroutines at the same time with async module """
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    An async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay.You will spawn wait_random
    n times with the specified max_delay

    Args:
        n (int)
        max_delay(int)

    Return:
        list of all the delays (float values). The list of
        the delays should be in ascending order without using
        sort() because of concurrency.
    """
    spawn_list = []
    delay_list = []
    for i in range(n):
        delayed_task = asyncio.create_task(wait_random(max_delay))
        delayed_task.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(delayed_task)
    for spawn in spawn_list:
        await spawn

    return (delay_list)
