from machine import Pin, I2C
from time import sleep
import ssd1306
from vl53l0x import VL53L0X

# OLED on I2C0
i2c_oled = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c_oled)

# TOF on I2C1
i2c_tof = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
tof = VL53L0X(i2c_tof)

# give time to initialise 
sleep(2)

# clear display and show on screen message 
oled.fill(0)
oled.text("Ready", 0, 0)
oled.show()

print("System started")


def get_reading_and_display():
    ''' function that read the distance and displays to the screen'''
    try:
        distance = tof.read_range_single_millimeters()
        print("Distance: {} mm".format(distance))
        oled.text("Distance:", 0, 14)
        # reset the row on the screen
        oled.fill_rect(0, 30, 128, 8, 0)
        # print to screen
        oled.text(f'{distance} mm', 0, 30)
        oled.show()
        return distance

    except Exception:
        oled.fill_rect(0, 30, 128, 8, 0)
        print("Out of range / no reading")
        oled.show()
        return -1
   
    
while True:
    get_reading_and_display()
    sleep(0.1)
