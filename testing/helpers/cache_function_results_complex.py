'''
Cache long running function results. If CACHE is set, will use the cached values instead of calling the function
Cache files are specific to the args passed. Args are hashed and added to the cache file name
'''
import os
import json

def cache_function_results(*args, **kwargs):
    '''
    Cache long running function results.  Used to make testing easier
    Function args are hashed and added to the cache name, so multiple calls with different args
    will result in multiple caches.  

    Cache name suffix is 40 characters.
    set environment variable CACHE=true to use the cached data
    '''

    def decorated_func(*args, **kwargs):
        # Can't use with pytest.
        if os.getenv('PYTEST_CURRENT_TEST'):
            return func(*args, **kwargs)
        
        # use args that are not complex objects to determine cache name.
        # Thought about using a hash so all of the args were covered, but that makes identifying cache files more difficult
        args_str = '_'.join([str(arg) for arg in args if isinstance(arg, (float, int, str))])
        kwargs_str = '_'.join([f'{key}={str(value)}' for key, value in kwargs.items() if isinstance(value, (float, int, str))])
        cache_suffix = f'{args_str}_{kwargs_str}'[:40]

        cache_option = os.getenv('CACHE')
        cache_file = f'cache/cache-{func.__name__}-{suffix}.json'
        if not cache_option:
            print(f'write {cache_file}')
            result = func((*args, **kwargs))
            with open(cache_file, 'w') as outfile
                json.dump(result, outfile, indent=4, default=str)
            return results

        else:
            try:
                with open(cache_file, 'r') as infile:
                    result = json.load(infile)
                print(f'read {cache_file}')
            except FileNotFoundError:
                print(f'{cache_file} does not exist to read')
                result = func((*args, **kwargs))
                with open(cache_file, 'w') as outfile
                    json.dump(result, outfile, indent=4, default=str)
                return results

    return decorated_func()           
