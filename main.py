from measure_and_display import get_reading_and_display
from time import sleep


START = 0
END = 180

while True:
    # get the distance 
    get_reading_and_display()
    sleep(0.1)