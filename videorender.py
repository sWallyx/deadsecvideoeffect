import numpy as np
import cv2

cap = cv2.VideoCapture('congratulations.mp4')
#cap = cv2.VideoCapture('output.avi')

#Calculate FPS
fps = cap.get(cv2.CAP_PROP_FPS)
print (format(fps))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MPEG')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
	ret, frame = cap.read()
	if ret==True:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# write the flipped frame
		out.write(frame)

		cv2.imshow('Congratulations T-Series',gray)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
out.release()
cv2.destroyAllWindows()