import os
import logging

def lambda_logging(default_level='INFO'):
    '''
    Lambda functions have existing logger. In order to test locally and when deployed to lambda
    the logging module must look for this.
    '''
    LOG_LEVEL = logging.getLevelName(os.environ.get("LOG_LEVEL", default_level))
    if logging.getLogger().handlers:
        logging.getLogger().setLevel(LOG_LEVEL)
    else:
        logging.basicConfig(level=LOG_LEVEL)
    LOG = logging.getLogger(__name__)
