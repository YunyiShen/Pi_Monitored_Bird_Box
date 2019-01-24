import Adafruit_DHT
# DHT11 test
print("DHT test...")
sensor = Adafruit_DHT.DHT11
pin1 = 17
pin2 = 16
humidity1, temperature1 = Adafruit_DHT.read_retry(sensor, pin1)
print("Humidity measured by sensor1 is:")
print(humidity1)
print("Temperature measured by sensor1 is:")
print(temperature1)

humidity2, temperature2 = Adafruit_DHT.read_retry(sensor, pin2)
print("Humidity measured by sensor2 is:")
print(humidity2)
print("Temperature measured by sensor2 is:")
print(temperature2)



## PIR test
print("PIR test...")
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.IN) #PIR


try:
    time.sleep(2) # to stabilize sensor
    for i in range(1,20):
        print(i)
        if GPIO.input(25):
            print("Motion Detected...")
            time.sleep(5) #to avoid multiple detection
        time.sleep(1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()


##PIcam test
from picamera import PiCamera
print("PIcam test...")
# from time import sleep
camera = PiCamera()
camera.start_preview()
time.sleep(5)
camera.capture("/home/pi/Desktop/Picamera_test.jpg")
camera.stop_preview()
