from measure_and_display import get_reading_and_display
from time import sleep
from bigmotor import rotate_base


STEPS = 100
readings = []
objects = []

# tower distances 
CLOSE_COLUMN = 800
MIDDLE_COLUMN = 1300
FAR_COLUMN = 1800

# get the distance 
for _ in range(STEPS):
    readings.append(get_reading_and_display())
    rotate_base(True)
    sleep(0.1)

# store prev state so we can keep track of if we are
# currently observing the object or not 
prev_state = 0
middle = []
count = 0
# offset so the array values line up with the readings
objects.append(0)
for i in range(STEPS-1):
    # use readings to identify if an object is being detected or not
    if abs(readings[i] - readings[i+1]) > 500: 
        prev_state = 0 if prev_state == 1 else 1
        if prev_state ==1:
            # number of consecutive 1s
            count +=1
        elif prev_state == 0 and count != 0:
            # store the middle of the tower readings
            middle.append(count // 2)
            count = 0
        objects.append(prev_state)
    else:
        objects.append(prev_state)
if count !=0:
    middle.append(count // 2)

obj = len(middle) -1 
current = STEPS -1
while current >= 0:
    # first edge of the object detected
    if objects[current] == 1:

        # skip to the middle of the obj
        for _ in range(middle[obj]):
                rotate_base(False)
                current-=1
        obj-=1
        # now find what sort of distance we are from the object
        curr_dist = readings[current]

        curr_choice = 'close'
        curr_choice_dist = abs(curr_dist - CLOSE_COLUMN)
        
        if abs(curr_dist - MIDDLE_COLUMN) < curr_choice_dist:
            curr_choice = 'middle'
            curr_choice_dist = abs(curr_dist - MIDDLE_COLUMN)
        
        if abs(curr_dist - FAR_COLUMN) < curr_choice_dist:
            curr_choice = 'far'

        
    #CALL FUNCTION 
    #Set_Catapult(curr_choice)
    #reset_Catapult()

    while objects[current] == 1:
        current-=1
        rotate_base(False)
        






