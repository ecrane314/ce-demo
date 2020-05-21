import google.cloud.logging
import logging

client = google.cloud.logging.Client()

client.get_default_handler()
client.setup_logging()

