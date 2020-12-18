import time

def timer(func):
    '''
    Decorator that prints out the clock runtime for a fuction
    To exclude sleep time, replace monotonic with process_time()
    '''
    def decorated_function(*args, **kwargs):
        start_time = time.monotonic()
        result = func(*args, **kwargs)
        duration = time.monotonic() - start_time
        print(f'TIMER {func.__name__}: {duration} seconds')
        return result

    return decorated_function()
