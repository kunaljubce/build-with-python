import asyncio
from asyncio import Future

# Basic implementation of Future
async def main_without_await():
    my_future = Future()
    # A newly created future doesn’t have any value because it doesn’t exist yet. 
    # In this state, the future is considered incomplete, unresolved, or not done.
    print(my_future.done())  # False. 

    # set a value for the future object by calling the set_result() method:
    my_future.set_result('Bright')

    # Once you set the value, the future is done. Calling the done() method of the future object in this stage returns True:
    print(my_future.done())  # True
    print(my_future.result()) # Bright

# asyncio.run(main_without_await())

# Implementation of Future with await
async def plan(my_future):
    '''First, define a coroutine that accepts a future and sets its value after 1 second:'''
    print('Planning my future...wait for 2 secs')
    await asyncio.sleep(2)
    my_future.set_result('Bright')

def create() -> Future:
    '''Second, define a create() function that schedules the plan() coroutine as a task and returns a future object:'''
    my_future = Future()
    print("Future object created...")
    asyncio.create_task(plan(my_future))
    return my_future

async def main():
    '''Third, call the create() function that returns a future, use the await keyword to wait for the future to return a result, and display it:'''
    my_future = create()
    result = await my_future

    print(result)

asyncio.run(main())
