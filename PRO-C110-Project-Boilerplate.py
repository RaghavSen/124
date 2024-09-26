# To Capture Frame
import cv2

# To process image array
import numpy as np

import tensorflow as tf

model = tf.keras.model.load_model('keras_model.h5')
# import the tensorflow modules and load the model



# Attaching Cam indexed as 0, with the application software
camera = cv2.VideoCapture(0)

# Infinite loop
while True:

	# Reading / Requesting a Frame from the Camera 
	status , frame = camera.read()

	# if we were sucessfully able to read the frame
	if status:

		# Flip the frame
		frame = cv2.flip(frame , 1)
		img = cv2.resize(frame,(100,100))

		samples_img = np.expand_dims(samples_img,axis=0)

		normalize_img = samples_img/255.0
		prediction = model.predict(normalize_img)
	    
		
	
		
		# expand the dimensions
		
		# normalize it before feeding to the model
		
		# get predictions from the model
		
		
		
		# displaying the frames captured
		cv2.imshow('feed' , frame)

		# waiting for 1ms
		code = cv2.waitKey(1)
		
		# if space key is pressed, break the loop
		if code == 32:
			break

# release the camera from the application software
camera.release()

# close the open window
cv2.destroyAllWindows()
