import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT
DHT_PIN = 4
from time import sleep, strftime, time
while True:
temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
if temp is not None:
    text = open('dataset.csv', 'w')
    data.write("{0}, {1}""\n".format(strftime('%Y:%m:%d %H/%M/%S'), str(value)))
    text.close()
else:
    print("Failed to read from sensor")
sleep(1)


