#!/usr/bin/env python3

"""
How to authenticate manually, explicitly, as in cron where don't know env
https://cloud.google.com/docs/authentication/production#create_service_account

Loggers and handlers explained
https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
https://www.youtube.com/watch?v=jxmzY9soFXg

Logging from python client, logging, export, and handler samples exist
https://cloud.google.com/logging/docs/quickstart-python#linux

API for Google Logging client library
https://googleapis.dev/python/logging/latest/index.html
"""

import logging

import google.cloud.logging
#from google.cloud.logging.handlers import CloudLoggingHandler


def write_logs():
    """Setup local logging, infer credentials and setup cloud logging
     write test events to both local and cloud logs"""
    #create logger and set level
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    #create a format, optional
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    #create file handler with path, set formatter
    file_handler = logging.FileHandler('python.log')
    file_handler.setFormatter(formatter)


    ###  CREATE HANDLER TO WRITE TO GCP CLOUD LOGS  ###
    #create cloud logging client
    client = google.cloud.logging.Client()

    #Create cloud handler and set formatter
    cloud_handler = google.cloud.logging.handlers.CloudLoggingHandler(client)
    cloud_handler.setFormatter(formatter)

    #add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(cloud_handler)
    print("write_logs() handlers: " + str(logger.handlers))


    logger.debug("This is a DEBUG item")
    logger.info("This is INFO log")
    logger.warning('This is a WARNING log message')
    logger.error("This is an ERROR")
    logger.critical("This is CRITICAL")


def write_logs_explicit_credentials():
    """Setup local logging, explicity define credentials and setup
     cloud logging, write test events to both local and cloud logs"""
    #create logger and set level
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    #create a format, optional
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    #create file handler with path, set formatter
    file_handler = logging.FileHandler('python.log')
    file_handler.setFormatter(formatter)

    #add handlers to logger
    logger.addHandler(file_handler)


    ###  CREATE HANDLER TO WRITE TO GCP CLOUD LOGS  ###
    #create cloud logging client
    try:
        client = google.cloud.logging.Client.from_service_account_json(\
            '/home/evancrane/crane-gcp_pi-water-plants.json')

        #Create cloud handler and set formatter
        cloud_handler = google.cloud.logging.handlers.CloudLoggingHandler(client)
        cloud_handler.setFormatter(formatter)

        #add cloud handler
        logger.addHandler(cloud_handler)
    except FileNotFoundError:
        logger.error('Cloud logger client not established')

    logger.info("Handlers: %s", logger.handlers)

    logger.debug("This is a DEBUG item")
    logger.info("This is INFO log")
    logger.warning('This is a WARNING log message')
    logger.error("This is an ERROR")
    logger.critical("This is CRITICAL")


if __name__ == "__main__":
    #write_logs()
    write_logs_explicit_credentials()
