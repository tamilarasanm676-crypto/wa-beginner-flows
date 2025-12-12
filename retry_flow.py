from prefect import flow, task
from random import randint

@task(retries=3, retry_delay_seconds=2)
def unstable_task():
    n = randint(1, 10)
    if n <= 7:
        raise Exception("Random failure!")
    else:
        print(f"Success! Random number was {n}")
        return n

@flow
def retry_example():
    result = unstable_task()
    print("Final result:", result)
