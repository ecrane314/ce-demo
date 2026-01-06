"""Pull public GCP pricing info from API and publish to topic
https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/skuGroups/list
"""

import subprocess
import json
from google.cloud import pubsub_v1

def publish_pricing_info(event, context):
    """
    Pulls public GCP pricing info from API using curl_get_pricing_skugroups.sh
    and publishes the results to a Pub/Sub topic.
    Args:
        event (dict): The Cloud Functions event payload.
        context (google.cloud.functions.Context): The Cloud Functions context.
    """
    project_id = "ce-demo1"
    topic_id = "sku-groups"
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)

    try:
        # Execute the shell script to get pricing data
        result = subprocess.run(
            ["./curl_get_pricing_skugroups.sh"],
            capture_output=True,
            text=True,
            check=True
        )
        pricing_data = result.stdout

        # Assuming the script returns valid JSON, parse it
        # If the script returns multiple JSON objects or a stream,
        # you might need more sophisticated parsing.
        try:
            json_data = json.loads(pricing_data)
            # Publish each item in the list as a separate message
            if isinstance(json_data, dict) and "skuGroups" in json_data:
                for item in json_data["skuGroups"]:
                    message_data = json.dumps(item).encode("utf-8")
                    print(f"Publishing message: {message_data}")
                    future = publisher.publish(topic_path, message_data)
                    print(f"Published message ID: {future.result()}")
            else:
                # If it's a single JSON object or not in expected format, publish as is
                message_data = pricing_data.encode("utf-8")
                future = publisher.publish(topic_path, message_data)
                print(f"Published message ID: {future.result()}")

        except json.JSONDecodeError:
            print("Warning: Script output is not valid JSON. Publishing as plain text.")
            message_data = pricing_data.encode("utf-8")
            future = publisher.publish(topic_path, message_data)
    finally:
        print("Finished function call")

if __name__ == "__main__":
    publish_pricing_info(None, None)