def enter_exit(func):
    '''Decorator to print function entry/exit methods'''
    def decorated_function(*args, **kwargs):
        print(f'{func.__name__} START')
        result = func(*args, **kwargs)
        print(f'{func.__name__} END')
        return result
    return decorated_function()