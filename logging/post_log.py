#!/usr/bin/env python3
"""
https://cloud.google.com/logging/docs/quickstart-python#linux
https://googleapis.dev/python/logging/latest/index.html
Use an export statement at shell to set your credentials before runtime
export GOOGLE_APPLICATION_CREDENTIALS=/home/evancrane/ce-demo2-bq-analyst.json
https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
"""

import logging

import google.cloud.logging


def write_log():
    """Write local test log and return logger object"""
    logging.basicConfig(filename='scratch.log', \
        format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)

    logging.debug("This is a DEBUG item")
    logging.info("This is INFO log")
    logging.warning('This is a WARNING log message')
    logging.error("This is an ERROR")
    logging.critical("This is CRITICAL")


#def upload_log(logger_name="test_water_log"):
def upload_log():
    """Write local log file to Google Cloud Logs """
    #Cloud logging client
    client = google.cloud.logging.Client()
    client.setup_logging(log_level=logging.debug)

    """
    # This log can be found in the Cloud Logging console under 'Custom Logs'.
    logger = client.logger(logger_name)

    # Make a simple text log
    logger.log_text('Hello, world! log_text() IN UPLOAD')

    # Simple text log with severity.
    logger.log_text('Goodbye, world! log_text(severity=ERROR)', severity='ERROR')

    # Struct log. The struct can be any JSON-serializable dictionary.
    logger.log_struct({
        'type': 'log_struct()',
        'name': 'King Arthur',
        'quest': 'Find the Holy Grail',
        'favorite_color': 'Blue'
    })
    """


if __name__ == "__main__":
    upload_log()
    write_log()