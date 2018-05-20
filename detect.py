#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import slackCapture as sc


# initialize GPIO inputs
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)

# initialize the state
detected = False
try:
	while True:
		i=GPIO.input(11)
		if i==0:
			if detected == True:
				print "All Clear"
		
			detected=False
		
		else:
			if detected == False:
				print "Detected",i
				sc.slack_capture()
				detected = True
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
			
		
