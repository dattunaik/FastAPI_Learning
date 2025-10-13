import time
from timeit import default_timer as timer 


def run_task(name, seconds):
    print(f'{name} started at {timer()}')
    time.sleep(seconds)
    print(f'{name} ended at {timer()}')


start = timer()
run_task('TASK 1', 2)
run_task('TASK 2', 1)
run_task('TASK_3', 3)

print(f'\n Total time taken: {timer()-start:.2f} s')