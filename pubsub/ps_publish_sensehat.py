#publish sense hat to a gcp pub/sub/topic
from google.cloud import pubsub_v1
from sense_hat import SenseHat
import time

#prepare sense client
sense = SenseHat()
sense.clear()

#prepare publisher client
pub = pubsub_v1.PublisherClient()
topic_path = pub.topic_path('ce-demo2', 'iot-data')
n=0

while n < 1000:
    temp = sense.get_temperature()
    print("temp: "+ str(temp))

    humidity = sense.get_humidity()
    print("humidity: "+ str(humidity))
    print("Trial: "+str(n))
    n += 1

    pub.publish(topic_path, b'This is Temperature in Celcius: +str(n)', Temperature=str(temp))
    time.sleep(2)

