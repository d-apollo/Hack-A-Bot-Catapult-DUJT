from measure_and_display import get_reading_and_display
from time import sleep


STEPS = 1
readings = []
objects = []
# get the distance 
for _ in range(STEPS):
    readings.append(get_reading_and_display())
    #rotate_base(True)
    sleep(0.1)

# store prev state so we can keep track of if we are
# currently observing the object or not 
prev_state = 0

# offset so the array values line up with the readings
objects.append(0)
for i in range(STEPS-1):
    if abs(readings[i] - readings[i-1]) > 500: 
        prev_state = 0 if prev_state == 1 else 0
        objects.append(prev_state)
    else:
        objects.append(prev_state)





