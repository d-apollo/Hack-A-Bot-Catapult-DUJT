from machine import Pin, I2C
from time import sleep
import ssd1306
from vl53l0x import VL53L0X


# OLED on I2C0
i2c_oled = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
print(i2c_oled.scan())


oled = ssd1306.SSD1306_I2C(128, 64, i2c_oled)


# TOF on I2C1
i2c_tof = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
tof = VL53L0X(i2c_tof)

sleep(2)

oled.fill(0)
oled.text("Ready", 0, 0)
oled.show()

print("System started")

while True:

    try:
        distance = tof.read_range_single_millimeters()
        print("Distance: {} mm".format(distance))
        oled.text("Distance:", 0, 20)
        oled.text(str(distance) + " mm", 0, 40)

    except Exception:
        print("Out of range / no reading")
        oled.text("No reading", 0, 30)

    oled.show()
    sleep(0.1)

