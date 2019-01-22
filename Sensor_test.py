import Adafruit_DHT
pin_inner = 17
pin_outer = 27
sensor = Adafruit_DHT.DHT11
humidity_inner , temperature_inner = Adafruit_DHT.read_retry(sensor,pin_inner)
humidity_outer , temperature_outer = Adafruit_DHT.read_retry(sensor,pin_outer)

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(100)
camera.capture('/home/pi/Desktop/insidebox.jpg')
camera.stop_preview()