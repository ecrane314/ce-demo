#!/usr/bin/env python3
"""
https://cloud.google.com/logging/docs/quickstart-python#linux
https://googleapis.dev/python/logging/latest/index.html
Use an export statement at shell to set your credentials before runtime
export GOOGLE_APPLICATION_CREDENTIALS=/home/evancrane/ce-demo2-bq-analyst.json
https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
"""

import logging
import os

from google.cloud import logging as glogging
#from google.auth import jwt


def write_log():
    """Write local test log"""
    logging.basicConfig(filename='scratch.log', \
        format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
        #encoding='utf-8'  avail in python 3.9

    logging.debug("This is a Debug item")
    logging.info("This is info log")
    logging.warning('This is a warning log message')
    logging.error("This is an error")
    logging.critical("This is critical, STOP")


def upload_log(logger_name="test_log"):
    """Write local log file to Google Cloud Logs """
    client = glogging.Client()

    #Talks to logger? Confirm what they do
    #handler =  client.get_default_handler()
    #client.setup_logging()

    # This log can be found in the Cloud Logging console under 'Custom Logs'.
    logger = client.logger(logger_name)

    handler = client.setup_logging()

    # Make a simple text log
    logger.log_text('Hello, world!')

    # Simple text log with severity.
    logger.log_text('Goodbye, world!', severity='ERROR')

    # Struct log. The struct can be any JSON-serializable dictionary.
    logger.log_struct({
        'name': 'King Arthur',
        'quest': 'Find the Holy Grail',
        'favorite_color': 'Blue'
    })

    #service_account = json.load(open("/home/evancrane/ce-demo2-log.json"))
    #audience = "https://www.googleapis.com/auth/logging.write"
    #credentials = jwt.Credentials.from_service_account_info(
    #    service_account, audience=audience
    #)


if __name__ == "__main__":
    write_log()
