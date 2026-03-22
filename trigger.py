from machine import Pin, PWM
import time

#this needs to be adjusted for the right pins
servo1 = PWM(Pin(15))
servo1.freq(50)

#same function youve seen before to turn angles into frequency
def set_servo_angle(angle):
    min_us = 500
    max_us = 2500
    us = min_us + (angle / 180) * (max_us - min_us)
    duty = int(us / 20000 * 65535)
    servo1.duty_u16(duty)

#main trigger function that calls everything else pretty much. 
#moves out of launching arms way, waits 3 seconds and moves back in to secure.
def trigger_shot():
    current_angle = 0
    set_servo_angle(current_angle)
    current_angle += 180
    set_servo_angle(current_angle)

    time.sleep(4)  # wait 3 seconds

    current_angle += 180
    set_servo_angle(current_angle)