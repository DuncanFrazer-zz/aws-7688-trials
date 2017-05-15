from pyfirmata import Arduino, util
from time import sleep
 
board = Arduino('/dev/ttyS0')
print "Start Toggling GPIO"
board.digital[5].write(1)
sleep(0.5)
board.digital[5].write(0)
