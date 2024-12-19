import time
import RPi.GPIO as GPIO
from azure.storage.blob import BlobServiceClient
from picamera2 import Picamera2
import os
import logging

# set up errors.txt file to store any errors
logging.basicConfig(filename='errors.txt', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def log_error(exception):
	logging.error(f"Error:{exception}")
	print(f"Error:{exception}")

WDT_timeout = 120
last_kick_time = time.time()
def reset_WDT():
	global last_kick_time
	last_kick_time = time.time()

def check_WDT():
	global last_kick_time
	if time.time() - last_kick_time > WDT_timeout:
		print("WDT expired.")
		log_error("WDT Reset")
		return True
	return False

#set up button
Button_Pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(Button_Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# set up blob connection
connection_string = "DefaultEndpointsProtocol=https;AccountName=chessimages;AccountKey=BVfdVF+YuBZzNd1qM+oel02RJuScISiwsa+dLstiEJKY0MhH6OD+rSSd/1Nl6iVwyRfai09lgJiO+ASt23PaWA==;EndpointSuffix=core.windows.net"
container_name = "chess"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
blob_client = blob_service_client.get_blob_client(container=container_name, blob="chess_upload.jpg")

# set up picam2
picam2 = Picamera2()
camera_config = picam2.create_still_configuration()
picam2.configure(camera_config)
# start cam
picam2.start()
time.sleep(2)

# if the button is pressed, then
def on_button_press():
	
	
	# take picture
	picam2.capture_file("chessCap.jpg")
	image_path = "/home/cosmo/Desktop/Test/chessCap.jpg"
	
	with open(image_path, "rb") as data:
		blob_client.upload_blob(data, overwrite=True)
		print("Upload successful")


try:
	
	#keep the script running
	while True:
		reset_WDT()
		if(GPIO.input(Button_Pin)==0):
			print("Button Pressed")
			on_button_press()
		if check_WDT():
			print("resetting system")
			break
		
		time.sleep(0.1)
except KeyboardInterrupt:
	#logger.info("Exiting...")
	log_error("Program Ended")
	picam2.stop()
	print("Done")
