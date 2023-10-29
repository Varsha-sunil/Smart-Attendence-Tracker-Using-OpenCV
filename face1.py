import cv2
import numpy as np

import face_recognition

img008 = face_recognition.load_image_file('I')
img008 = cv2.cvtColor(img008, cv2.COLOR_BGR2RGB)

cv2.imshow('AMULYA',img008)
cv2.waitkey(0)
