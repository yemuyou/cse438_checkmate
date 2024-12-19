import cv2

cap = cv2.VideoCapture(3)

if not cap.isOpened():

	print("Cannot open camera")
	exit()
	

while True:
		ret, frame = cap.read()
		
		if not ret:
			print("CAn't retrieve frame (stream ended?) Exiting now...")
			break
		
		cv2.imshow('CAmera Feed', frame)
		
		if cv2.waitKey(1) == ord('q'):
			break
			

cap.release()
cv2.destroyAllWIndows()
