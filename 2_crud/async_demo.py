import time 
import asyncio
from timeit import default_timer as timer

async def run_task(name, seconds):
    print(f'{name} started at {timer()}')
    await asyncio.sleep(seconds)
    print(f'{name} ended at {timer()}')


async def main():
    start = timer()
    await asyncio.gather(
        run_task('T1', 2),
        run_task('T2', 1),
        run_task('T3', 4),
        run_task('T4', 3)
    )
   

    print(f'Total time taken for the tasks to complete is {timer()-start:.2f}seconds')

asyncio.run(main())