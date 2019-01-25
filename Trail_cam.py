import RPi.GPIO as GPIO
import time
from picamera import PiCamera


print("Trail Camera Test...")
GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.IN) #PIR

camera = PiCamera()

try:
    time.sleep(2) # to stabilize sensor
    for i in range(1,20):
        print(i)
        if GPIO.input(25):
            print("Motion Detected...")
			camera.start_preview()
			time.sleep(1)
			camera.stop_preview()
            time.sleep(5) #to avoid multiple detection
        time.sleep(1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()