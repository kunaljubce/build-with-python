import asyncio

async def get_some_values_from_io():
    # Some IO code which returns a list of values
    print("get_some_values_from_io() going to sleep...")
    await asyncio.sleep(1)
    print("get_some_values_from_io() awake now...")
    return [1, 2, 3, 4, 5]

vals = []

async def fetcher():
    while True: # Makes fetcher() run in an infinite loop
        print("Inside Fetcher now...")
        io_vals = await get_some_values_from_io()
        print("Inside Fetcher, received io_vals...")

        for val in io_vals:
            vals.append(val)
            # await asyncio.sleep(1) # This await would put fetcher into sleep and pass the control via EL to monitor. So on every iteration of append, monitor() gets called. 
        print(vals)

async def monitor():
    while True: # Makes monitor() run in an infinite loop
        print("Inside Monitor, printing len(vals): ", len(vals))
        print("Monitor going to sleep...")
        await asyncio.sleep(1)

async def main():
    #t1 = asyncio.create_task(fetcher())
    #t2 = asyncio.create_task(monitor())
    #await asyncio.gather(t1, t2)
    await asyncio.gather(fetcher(), monitor()) # 1 line that does the same as the above 3 lines

    '''
    Even though both fetcher and monitor access the global variable vals they do so in two tasks that are running in the same event loop. 
    For this reason it is not possible for the print statement in monitor to run unless fetcher is currently asleep waiting for io. 
    This means that it is not possible for the length of vals to be printed whilst the for loop is only part-way through running. 
    So if the get_some_values_from_io always returns 5 values at a time then the printed length of vals will always be a multiple of 5. 
    It is simply not possible for the print statement to execute at a time when vals has a non-multiple of ten length.

    =========OUTPUT=========
    Inside Fetcher now...
    get_some_values_from_io() going to sleep...
    Inside Monitor, printing len(vals):  0
    Monitor going to sleep...
    get_some_values_from_io() awake now...
    Inside Fetcher, received io_vals...
    [1, 2, 3, 4, 5]
    Inside Fetcher now...
    get_some_values_from_io() going to sleep...
    Inside Monitor, printing len(vals):  5
    Monitor going to sleep...
    get_some_values_from_io() awake now...
    Inside Fetcher, received io_vals...
    [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    '''

asyncio.run(main())
