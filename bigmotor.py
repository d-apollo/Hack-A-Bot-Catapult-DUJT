from machine import Pin
from time import sleep, sleep_us

#Pins on the drivers that affect direction and step pulse
DIR = Pin(19, Pin.OUT)
STEP = Pin(20, Pin.OUT)
GP = Pin(26, 1)

#Motor driver information
STEP_ANGLE = 1.8      # degrees per step

#Function takes boolean argument to decide direction
def rotate_base(clockwise=True):
    print('reached')
    #decides direction
    DIR.value(1 if clockwise else 0)
    #does a step, 1.8 degrees
    STEP.value(1)
    #delay to allow driver to register
    sleep_us(10) 
    #stops step 
    STEP.value(0)
    #delay before next loop
    sleep_us(10)

def __init__():
    while True:
        rotate_base(True)
        sleep(0.1)

__init__()