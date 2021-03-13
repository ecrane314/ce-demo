#!/usr/bin/env python3

"""
https://cloud.google.com/logging/docs/quickstart-python#linux
https://googleapis.dev/python/logging/latest/index.html
https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
https://www.youtube.com/watch?v=jxmzY9soFXg
"""

import logging

import google.cloud.logging
#from google.cloud.logging.handlers import CloudLoggingHandler


def write_logs():
    """Setup logging and write test events to local log file"""
    #create logger and set level
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    #create a format, optional
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    #create file handler with path, set formatter
    file_handler = logging.FileHandler('python.log')
    file_handler.setFormatter(formatter)


    """Create handler to write to Google Cloud Logs """
    #create cloud logging client
    client = google.cloud.logging.Client()
    
    #Create cloud handler and set formatter
    cloud_handler = google.cloud.logging.handlers.CloudLoggingHandler(client)
    cloud_handler.setFormatter(formatter)

    #add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(cloud_handler)
    print(logger.handlers)
    #TODO Not sure which this gets: get_default_handler()
    #logger.addHandler = client.get_default_handler()


    logger.debug("This is a DEBUG item")
    logger.info("This is INFO log")
    logger.warning('This is a WARNING log message')
    logger.error("This is an ERROR")
    logger.critical("This is CRITICAL")


if __name__ == "__main__":
    write_logs()
