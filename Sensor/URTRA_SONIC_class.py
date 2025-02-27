#URTRA SONIC class
import RPi.GPIO as GPIO
import time

class URTRA_SONIC_SENSOR:
    #GPIO pin setup
    def __init__(self,sense_pin = 17,read_pin = 27):
        self.sense_pin = sense_pin
        self.read_pin = read_pin
        
    def sense_urtra_sonic(self):
        GPIO.output(self.sense_pin,GPIO.LOW)

        time.sleep(0.3)
        GPIO.output(self.sense_pin,True)
        time.sleep(0.00001)
        GPIO.output(self.sense_pin,False)

        while GPIO.input(self.read_pin) == 0:
            signal_off = time.time()
        while GPIO.input(self.read_pin) == 1:
            signal_on = time.time()
            time_passed = signal_on - signal_off

        distance = 34000 * time_passed / 2
        return distance 



