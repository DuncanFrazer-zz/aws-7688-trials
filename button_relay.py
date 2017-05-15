from pyfirmata import Arduino, util
from pyfirmata.util import Iterator
from time import sleep
import os
 
board = Arduino('/dev/ttyS0')
iterator = Iterator(board)
iterator.start()

button = board.get_pin('d:6:i')
button.enable_reporting()

def main():
	last=0
	count=0

	try:
		print ("monitoring button")
		for i in range(100):
		   # The return values are: True False, and None
		   if str(button.read()) == 'True':
			if last == 0:
			       print ("Button pressed")
			       board.digital[5].write(1)
			       last=1
			       count+=1
			       print (count)
		   elif str(button.read()) == 'False':
			if last == 1:
#			       print ("Button not pressed")
			       board.digital[5].write(0)
			       last=0
		   sleep(0.5)
	except KeyboardInterrupt:
		print ("exiting")
		os._exit(0)

if __name__ == '__main__':
	main()
