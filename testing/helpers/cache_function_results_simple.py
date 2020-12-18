'''
Cache long running function results. If CACHE is set, will use the cached values instead of calling the function
This version only works for a function that is called once, or is called multiple times but returns the same results.
'''
import os
import json

def cache_function_results(func):
    '''Cache long running function results. Used to make testing easier'''
    def decorated_func(*args, **kwargs):
        cache_option = os.getenv('CACHE')
        cache_file = f'cache/cache-{func.__name__}.json'
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
