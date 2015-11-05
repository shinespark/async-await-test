# coding: utf-8
import asyncio


def fizzbuzz(i):
    if i == 15:
        return 'FizzBuzz'
    if i % 5 == 0:
        return 'Buzz'
    if i % 3 == 0:
        return 'Fizz'

    return str(i)


async def task_fizzbuzz(prefix):
    for x in range(1, 10):
        print(prefix + '{}:'.format(str(x)) + fizzbuzz(x))
    return None

loop = asyncio.get_event_loop()

tasks = asyncio.wait([task_fizzbuzz(str(i) + ':') for i in range(1, 100000)])
loop.run_until_complete(tasks)
loop.close()
