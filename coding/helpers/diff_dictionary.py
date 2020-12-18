from deepdiff import DeepDiff

def diff_dictionary(dict1, dict2):
    '''Diff two dictionaries, ignoring list ordering'''
    return DeepDiff(dict1, dict2, ignore_order=True, report_repetition=True, view='text')