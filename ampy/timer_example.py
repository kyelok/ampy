# Basic Timer usage with a callback
# Author: Kyel Ok

import machine
import time
import uos
import micropython
from machine import Timer

# TimerCallback object
class TimerCallback:
    def __init__(self, pin):
        # some memory allocated within the object
        # in current implementation, the callback function can't allocate memory
        self.tick = 0

        # create a timer object
        self.timer = Timer(-1)

        # initialize a timer with callback period of 200        
        self.timer.init(period=200, mode=Timer.PERIODIC, callback=self.print_message)

    # the callback function
    def print_message(self, *args):
        self.tick = self.tick + 1
        print('%d' % self.tick)

# alloc ememergency buff
micropython.alloc_emergency_exception_buf(100)

TimerCallback(0)

print ('wait1')
time.sleep(1)
print ('wait2')
time.sleep(1)
print ('wait3')
time.sleep(1)
print ('done\n')