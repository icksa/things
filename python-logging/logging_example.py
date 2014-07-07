import logging
import logging.handlers
import sys

def setup_logger():
    formatter = logging.Formatter('%(asctime)s %(levelname)s [%(name)s] %(message)s')
    handler = logging.handlers.RotatingFileHandler(filename="logging_example.log",
                                                   maxBytes=10*2**10, 
                                                   backupCount=3,
                                                   encoding='utf-8')

    # Note that backupCount of 3 means that the following files will be generated:
    #   logging_example.log
    #   logging_example.log.1
    #   logging_example.log.2
    #   logging_example.log.3
    
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel('INFO')

def test_function():
    logger = logging.getLogger('test_function')

    logger.debug('Message')
    logger.info('Message')
    logger.warn('Message')
    logger.error('Message')
    logger.critical('Message')

def main():
    for i in xrange(100):
        test_function()
    raise Exception('Oh no!')

if __name__ == '__main__':
    setup_logger()
    logger = logging.getLogger(__name__)
    logger.error('Message from MAIN')

    # This code will ensure that we exit with an appropriate error
    # code and will ensure that any exception is caught and written to
    # the log:
    status = 1
    try:
        status = main()
    except:
        logging.exception('Unrecoverable Error Detected')
    finally:
        sys.exit(status)
