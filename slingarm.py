from machine import Pin, PWM
import time

#pin and servo frequency logic
servo2 = PWM(Pin(3))
servo2.freq(50)

current_angle = 0  # starts arm at 0°, where it should be positioned straight down


#logic for translating angle into actual servo pulse movement
def set_servo_angle(angle):
    min_us = 500
    max_us = 2500
    angle = 180 - angle
    us = min_us + (angle / 180) * (max_us - min_us)
    duty = int(us / 20000 * 65535)
    servo2.duty_u16(duty)

#resets catapult to 0 degree angle for next firing by decrementing by 60
def reset_catapult():
    global current_angle
    while current_angle > 0:
        current_angle -= 20
        if current_angle < 0:
            current_angle = 0
        set_servo_angle(current_angle)
        time.sleep(0.2)  


def set_catapult(distance):
    global current_angle

    if distance == "far":
            current_angle = 360
            set_servo_angle(current_angle)
    elif distance == "middle":
        for i in range(6):
            current_angle = current_angle + 20
            set_servo_angle(current_angle)
            time.sleep_ms(100)
    else:
        for i in range(3):
            current_angle = current_angle + 20
            set_servo_angle(current_angle)
            time.sleep_ms(100)


def __init__():
    while True:
        set_catapult("far")
__init__()