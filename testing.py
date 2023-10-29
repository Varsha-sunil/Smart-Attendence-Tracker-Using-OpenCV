import face_recognition
import cv2
import numpy as np

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
print(11)
video_capture = cv2.VideoCapture(0)

# # Load a sample picture and learn how to recognize it.
# img008 = face_recognition.load_image_file("Images/1KS19EC008_AMULYA_R.jpg")
# img_008_encoding = face_recognition.face_encodings(img008)[0]
# print(22)
# # Load a second sample picture and learn how to recognize it.
# img050 = face_recognition.load_image_file("Images/1KS19EC050_Monisha_B_K.jpg")
# img_050_encoding = face_recognition.face_encodings(img050)[0]
# #
# # # Load a third sample picture and learn how to recognize it.
# # img051 = face_recognition.load_image_file("Images/1KS19EC051_Anila_D.jpg")
# # img_051_encoding = face_recognition.face_encodings(img051)[0]
# #
# # # Load a fourth sample picture and learn how to recognize it.
# # img053 = face_recognition.load_image_file("Images/1KS19EC053_Nisarga_K.jpg")
# # img_053_encoding = face_recognition.face_encodings(img053)[0]
# #
# # # Load a fifth sample picture and learn how to recognize it.
# # img054 = face_recognition.load_image_file("Images/1KS19EC054_Nithin_D.jpg")
# # img_054_encoding = face_recognition.face_encodings(img054)[0]
# # print(33)
# # # Load a sixth sample picture and learn how to recognize it.
# # img055 = face_recognition.load_image_file("Images/1KS19EC055_Pavan_Kumar_G_R.jpg")
# # img_055_encoding = face_recognition.face_encodings(img055)[0]
# #
#Load a seventh sample picture and learn how to recognize it.
#img061 = face_recognition.load_image_file("Images/1KS19EC061_Prashanth_S_K.jpg")
#img_061_encoding = face_recognition.face_encodings(img061)[0]
#
# # # Load a eigth sample picture and learn how to recognize it.
# # img064 = face_recognition.load_image_file("Images/1KS19EC064_Priyanka_K.jpg")
# # img_064_encoding = face_recognition.face_encodings(img064)[0]
# #
# # # Load a ninth sample picture and learn how to recognize it.
# img065 = face_recognition.load_image_file("Images/1KS19EC065_Radhakrishna_L.jpg")
# img_065_encoding = face_recognition.face_encodings(img065)[0]
# #
# # # Load a tenth sample picture and learn how to recognize it.
# # img066 = face_recognition.load_image_file("Images/1KS19EC066_Rajalakshmi.S.jpg")
# # img_066_encoding = face_recognition.face_encodings(img066)[0]
# #
# #
# # # Load a 11th sample picture and learn how to recognize it.
#img069 = face_recognition.load_image_file("Images/1KS19EC069_Rohan_K_R.jpg")
#img_069_encoding = face_recognition.face_encodings(img069)[0]
# #
# # # Load a 12th sample picture and learn how to recognize it.
# # img070 = face_recognition.load_image_file("Images/1KS19EC070_Bharatesh.jpg")
# # img_070_encoding = face_recognition.face_encodings(img070)[0]
# #
# # # Load a 13th sample picture and learn how to recognize it.
# # img078 = face_recognition.load_image_file("Images/1KS19EC078_SHAMITHA.jpg")
# # img_078_encoding = face_recognition.face_encodings(img078)[0]
# #
# # # Load a 14th sample picture and learn how to recognize it.
# # img079 = face_recognition.load_image_file("Images/1KS19EC079_Shashank_Kashyap_H_R.jpg")
# # img_079_encoding = face_recognition.face_encodings(img079)[0]
# #
# # # Load a 15th sample picture and learn how to recognize it.
# # img081 = face_recognition.load_image_file("Images/1KS19EC081_Shreyams_D_K.jpg")
# # img_081_encoding = face_recognition.face_encodings(img081)[0]
# #
# # # Load a 16th sample picture and learn how to recognize it.
# # img082 = face_recognition.load_image_file("Images/1KS19EC082_Shreyas_B_Aradhya.jpg")
# # img_082_encoding = face_recognition.face_encodings(img082)[0]
# #
# #Load a 17th sample picture and learn how to recognize it.
# img083 = face_recognition.load_image_file("Images/1KS19EC083_Shreyas_Gowda.jpg")
# img_083_encoding = face_recognition.face_encodings(img083)[0]
# #
# #
# # #Load a 18th sample picture and learn how to recognize it.
# # img084 = face_recognition.load_image_file("Images/1KS19EC084_Shreyas_V_Bharadwaj.jpg")
# # img_084_encoding = face_recognition.face_encodings(img084)[0]
#
#Load a 19th sample picture and learn how to recognize it.
#img085 = face_recognition.load_image_file("ImageS/1KS19EC085_SHUBHAM.jpg")
#img_085_encoding = face_recognition.face_encodings(img085)[0]

#Load a 20th sample picture and learn how to recognize it.
img092 = face_recognition.load_image_file("Images/1KS19EC092_Sumukha_Vasishta_M_R.jpg")
img_092_encoding = face_recognition.face_encodings(img092)[0]


#Load a 22nd sample picture and learn how to recognize it.
#img098 = face_recognition.load_image_file("Images/1KS19EC098_Theerthana_SR.jpg")
#img_098_encoding = face_recognition.face_encodings(img098)[0]
#
#
#



# Create arrays of known face encodings and their names
# known_face_encodings = [img_008_encoding,img_050_encoding,img_051_encoding,img_053_encoding,img_054_encoding,
#                         img_055_encoding,img_061_encoding,img_064_encoding, img_065_encoding,img_066_encoding,
#                         img_069_encoding,img_070_encoding,img_078_encoding,img_079_encoding,img_081_encoding,
#                         img_082_encoding,img_083_encoding,img_084_encoding,img_085_encoding,img_092_encoding,
print( img_092_encoding)

