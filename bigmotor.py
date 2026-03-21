from machine import Pin
import time

#Pins on the drivers that affect direction and step pulse
DIR = Pin(3, Pin.OUT)
STEP = Pin(2, Pin.OUT)

#Motor driver information
STEP_ANGLE = 1.8      # degrees per step

#Function takes boolean argument to decide direction
def rotate_base(clockwise=True):

    #decides direction
    DIR.value(1 if clockwise else 0)
    #does a step, 1.8 degrees
    STEP.value(1)
    #delay to allow driver to register
    time.sleep_us(10) 
    #stops step 
    STEP.value(0)
    #delay before next loop
    time.sleep_us(10)
