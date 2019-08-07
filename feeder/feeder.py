import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import datetime
import json
from picamera import PiCamera

def getTepHum(sensor,pin):
    humidity, temperature = Adafruit_DHT.read_retry(eval("Adafruit_DHT."+sensor), pin) # reading environment
    res = {
           "Humidity" : humidity,
           "Temperature" : temperature,
         }
    return res

def main()
    err_count = 0
    pic_count = 1
    try:
        with open('config.json', 'r', encoding='utf-8') as config_json:
            config = json.load(config_json) # config for pins, maxmum error count, path to save, etc.
    except IOError as e:
        print(e)
        print("Fatal: fail to load config file.")
        return 0 # fatal     
    config_json.close() # close config file
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(config["PIR"], GPIO.IN) #PIR set up
    time.sleep(2) # to stabilize sensor
    last_time = datetime.datetime.now() # record time for compare
    
    while (err_count <= config["max_error"]):
        try:
            if GPIO.input(config["PIRpin"]):
                camera.capture(config['picture_dir']+'/'+str(datetime.datetime.now())+".jpg")
                pic_count += 1
                time.sleep(config['det_interval']) #to avoid multiple detection
        except:
            GPIO.cleanup()
            with open('errlog.txt', 'w', encoding='utf-8') as err_log:
                err_log.write(str(datetime.datetime.now())+' PIR sensor error detected\n')
            err_log.close()
            err_count += 1
        
        current_time = datetime.datetime.now()
        if ((current_time-last_time).total_seconds())>=config["log_interval"]:  # log temp etc. if time is long encough 
            
            for i in range(1,config['number_DHTsensors']): # can be any type of DHT sensors, 
                
                env = getTepHum(config['DHTsensor'][i],config['DHTpin'][i])
                env['time'] = current_time
                try : 
                    with open('DHTsensor_'+str(i)+'_data.json','w','utf-8') as data_log:
                    json.dump(env,data_log)
                except IOError as e:
                    with open('errlog.txt', 'w', encoding='utf-8') as err_log:
                        err_log.write(str(datetime.datetime.now())+' DHT sensor '+str(i)+' error '+e+'\n')
                    err_count += 1
                    err_log.close()
                data_log.close()
            last_time = current_time
        time.sleep(config["loop_interval"])
    print("number of errors exceed "+config['max_error']+'/n')
    return 0




if __name__ == '__main__':
    main()
        
