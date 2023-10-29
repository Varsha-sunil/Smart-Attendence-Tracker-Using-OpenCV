import face_recognition
import cv2
import numpy as np


#Load a 19th sample picture and learn how to recognize it.
img085 = face_recognition.load_image_file("Images/1KS19EC085_SHUBHAM.jpg")
img085 = cv2.c
img_085_encoding = face_recognition.face_encodings(img085)[0]

cv2.imshow("Shubham",img085)
cv2.waitKey(0)
cv2.destroyAllWindows()
