import time
import RPi.GPIO as GPIO

Button_Pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(Button_Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


try:
	#keep the script running
	while True:
		if(GPIO.input(Button_Pin)==0):
			print("Button Pressed")
		#print("Button State:", GPIO.input(Button_Pin))
		
		
		time.sleep(0.1)
except KeyboardInterrupt:
	#logger.info("Exiting...")
	print("Done")
