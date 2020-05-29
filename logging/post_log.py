#!/usr/bin/env python
"""
https://cloud.google.com/logging/docs/quickstart-python#linux
Use this export statement at shell to set your credentials before runtime
export GOOGLE_APPLICATION_CREDENTIALS=/home/evancrane/ce-demo2-bq-analyst.json
"""

#TODO Logging within Python?  https://realpython.com/python-json/
#import json
#import logging

#https://googleapis.dev/python/logging/latest/index.html
from google.cloud import logging
from google.auth import jwt

null="""
service_account = json.load(open("/home/evancrane/ce-demo2-log.json"))
audience = "https://www.googleapis.com/auth/logging.write"
credentials = jwt.Credentials.from_service_account_info(
    service_account, audience=audience
)
"""

def write_log(logger_name = "test_log"):
    client = logging.Client()

#TODO Unclear what these do or whether they're needed
#    handler =  client.get_default_handler()
#   client.setup_logging()


    # This log can be found in the Cloud Logging console under 'Custom Logs'.
    logger = client.logger(logger_name)

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

if __name__ == "__main__":
    write_log()
