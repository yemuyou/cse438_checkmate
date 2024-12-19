import time
import os
from datetime import datetime
import logging
from gpiozero import Button
import RPi.GPIO as GPIO
import cv2
from azure.storage.blob import BlobServiceClient, BlobClient
from azure.core.exceptions import AzureError
import traceback


# Configure logging
#logging.basicConfig(level = logging.INFO)
#logger = logging.getLogger(_name_)

# Azure storage configuration
# Replace with your actual connection str and container name
AZURE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=chessimages;AccountKey=BVfdVF+YuBZzNd1qM+oel02RJuSclSiwsa+dLstiEJKY0MhH6OD+rSSd/1Nl6iVwyRfai09lgJiO+ASt23PaWA==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "chess"

try:
	blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
	container_client = blob_service_client.get_container_client(CONTAINER_NAME)
	if not container_client.exists():
		container_client.create_container()
except AzureError as e:
	#logger.error(f"Failed to connect to Azure Blob Storage: {e}")
	exit(1)

# Initialize picamera2	
try:
	picam2 = Picamera2()
	# Config the camera for still images
	picam2.configure(picam2.create_still_configureation(main={"format":"RGB888"}))
	picam2.start()
	time.sleep(2)
except Exception as e:
	continue
		
# Intialize the button on GPIO17 with internal pull up
#button = Button(17, pull_up=True, bounce_time=0.1)
Button_Pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(Button_Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def capture_and_upload():
	# Capture current timestamp and filename
	timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
	image_filename = f"image_{timestamp}.jpg"
	
try:
	#logger.info("Capturing image...")
	#capture a frame as a NumPy array using picamera2
	frame = picam2.capture_array()
		
	# Convert the frame to BGR formate for OpenCV
	# picamera2 output is usually RGB, OpenCV uses BGR but
	# for just saving, this might not be necessary
		
	# Save image locally using OpenCV
	cv2.imwrite(image_path, frame)
	#logger.info(f"Image saved locally at {image_path}")
		
	# Uploading to Blob storage
	#logger.info("Uploading to Azure Blob Storage")
	blob_client = container_client.get_blob_client(image_filename)
		
	with open(image_path, "rb") as data:
		blob_client.upload_blob(data, overwrite=True)
			
	#logger.info("Upload Sucessful")
		
	#clean up local files
	os.remove(image_path)
except Exception as e:
	exit(1)
	
def on_button_pressed():
	#logger.info("Button pressed, capturing and uploading image.")
	capture_and_upload()
	
	#button.when_pressed = on_button_pressed
	
	#logger.info("System read. Press the button to capture and upload an image")
	
try:
	#keep the script running
	while True:
		if(GPIO.input(Button_Pin)==0):
			print("Button Pressed")
			on_button_pressed()
			
			
		time.sleep(0.5)
except KeyboardInterrupt:
	exit(1)
finally:
	picam2.stop()
	picam2.close()
